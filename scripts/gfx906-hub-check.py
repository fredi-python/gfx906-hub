#!/usr/bin/env python3
"""Nightly refresh of the MI50 / gfx906 hub status files.

Reads repos/tracked.json, asks the GitHub API for each tracked repo's head,
last push and latest version (release, else newest tag), then rewrites:

  README.md        the per-category summary tables and refresh footer
  docs/STATUS.md   the full generated table and a "last computed" stamp
  data/last-seen.json  the baseline the next run diffs against
  CHANGELOG.md     one entry per head movement (root ref of each repo)

The script only touches files, never git. The workflow commits and pushes.
No third-party packages; Python 3.9+ (stdlib only).

Auth: GITHUB_TOKEN (or GH_TOKEN) is read from the environment. Unauthenticated
runs work but are limited to 60 requests/hour, and this script uses ~50.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
UA = "gfx906-hub-check"
ROOT = Path(__file__).resolve().parent.parent

README = ROOT / "README.md"
STATUS = ROOT / "docs" / "STATUS.md"
LAST_SEEN = ROOT / "data" / "last-seen.json"
CHANGELOG = ROOT / "CHANGELOG.md"
TRACKED = ROOT / "repos" / "tracked.json"


def api(path, params=None, allow_404=True):
    """GET a GitHub API path. Returns None for 404 when allow_404, else raises."""
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": UA,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    req = urllib.request.Request(url, headers=headers)
    last = None
    for _ in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code == 404 and allow_404:
                return None
            last = exc
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
    raise RuntimeError(f"{url}: {last}")


def day(iso):
    return iso[:10] if iso else None


def repo_meta(owner, name):
    meta = api(f"/repos/{owner}/{name}", allow_404=False)
    return meta


def repo_commit(owner, name, ref):
    quoted = urllib.parse.quote(ref, safe="")
    data = api(f"/repos/{owner}/{name}/commits/{quoted}", allow_404=False)
    return data["sha"], day(data["commit"]["committer"]["date"])


def path_commit(owner, name, ref, path):
    data = api(
        f"/repos/{owner}/{name}/commits",
        {"path": path, "sha": ref, "per_page": 1},
        allow_404=False,
    )
    if not data:
        return None, None
    return data[0]["sha"], day(data[0]["commit"]["committer"]["date"])


def repo_version(owner, name):
    """Latest release (tag name + URL); if none, newest tag (name only)."""
    rel = api(f"/repos/{owner}/{name}/releases/latest")
    if rel:
        return rel.get("tag_name"), rel.get("html_url")
    tags = api(f"/repos/{owner}/{name}/tags", {"per_page": 1})
    if tags:
        return tags[0]["name"], None
    return None, None


def categories(repo):
    return repo.get("categories") or [repo["category"]]


def row_link(repo, cat):
    return repo.get("block_links", {}).get(cat) or repo_link(repo)


def repo_link(repo):
    link = repo["remote"]
    if repo.get("ref", "HEAD") != "HEAD":
        link += "/tree/" + repo["ref"]
    return link


def version_cell(version, url, empty):
    if not version:
        return empty
    return f"[{version}]({url})" if url else version


def replace_marked(text, begin, end, body, blank_before_end=True):
    a = text.index(begin) + len(begin)
    b = text.index(end)
    tail = "\n\n" if blank_before_end else "\n"
    return text[:a] + "\n" + body.rstrip("\n") + tail + text[b:]


def parse_block_rows(readme_text, cat):
    """Return the ordered row URLs of an existing README category block."""
    try:
        start = readme_text.index(f"### {cat}\n")
    except ValueError:
        return []
    end = readme_text.find("\n### ", start + 1)
    marker = readme_text.find("<!-- HUB-STATUS:END -->", start)
    end = min(x for x in (end, marker) if x != -1)
    urls = []
    for line in readme_text[start:end].splitlines():
        m = re.match(r"^\| \[[^\]]*\]\(([^)]+)\)", line)
        if m:
            urls.append(m.group(1))
    return urls


def render_readme(readme_text, repos, obs, cat):
    rows = [r for r in repos if r.get("status", "active") == "active" and cat in categories(r)]
    by_link = {row_link(r, cat): r["id"] for r in rows}
    existing = [by_link[u] for u in parse_block_rows(readme_text, cat) if u in by_link]
    order = list(existing)
    for repo in rows:
        if repo["id"] in order:
            continue
        new_date = block_date(obs[repo["id"]], cat)
        pos = len(order)
        for i, rid in enumerate(order):
            if block_date(obs[rid], cat) < new_date:
                pos = i
                break
        order.insert(pos, repo["id"])

    by_id = {r["id"]: r for r in rows}
    lines = [
        f"### {cat}",
        "",
        "| repo | focus | updated | head | version |",
        "|---|---|---|---|---|",
    ]
    for rid in order:
        repo = by_id[rid]
        o = obs[rid]
        lines.append(
            "| [{o}/{n}]({link}) | {focus} | {date} | `{sha}` | {version} |".format(
                o=repo["owner"],
                n=repo["name"],
                link=row_link(repo, cat),
                focus=repo["focus"],
                date=block_date(o, cat),
                sha=block_sha(o, cat)[:8],
                version=version_cell(
                    block_version(o, cat)[0], block_version(o, cat)[1], "—"
                ),
            )
        )
    return "\n".join(lines)


def block_sha(obs, cat):
    return (obs.get("blocks") or {}).get(cat, {}).get("sha") or obs["sha"]


def block_date(obs, cat):
    return (obs.get("blocks") or {}).get(cat, {}).get("date") or obs["pushed_at"]


def block_version(obs, cat):
    # A monorepo's subproject rows share the repo-level version.
    return obs.get("version"), obs.get("version_url")


def render_status(repos, obs):
    lines = [
        "| repo | category | role | ref | head | updated | version | compare |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for repo in repos:
        o = obs[repo["id"]]
        prev = o.get("prev")
        compare = (
            f"https://github.com/{repo['owner']}/{repo['name']}/compare/{prev}...{o['sha']}"
            if prev
            else "-"
        )
        lines.append(
            "| {o}/{n} | {cats} | {role} | `{ref}` | `{sha}` | {updated} | {version} | {compare} |".format(
                o=repo["owner"],
                n=repo["name"],
                cats=", ".join(categories(repo)),
                role=repo["role"],
                ref=repo.get("ref", "HEAD"),
                sha=o["sha"][:8],
                updated=o["pushed_at"],
                version=version_cell(o.get("version"), o.get("version_url"), "-"),
                compare=compare,
            )
        )
    return "\n".join(lines)


def parse_changelog(text):
    """Return (intro, [(date, [entry, ...]), ...]) preserving newest-first order."""
    marker = "\n## "
    idx = text.find(marker)
    if idx == -1:
        return text.rstrip("\n"), []
    intro = text[:idx]
    sections = []
    for chunk in text[idx:].split(marker)[1:]:
        chunk = chunk.rstrip("\n")
        if not chunk.strip():
            continue
        lines = chunk.splitlines()
        date = lines[0].strip()
        entries = [ln for ln in lines[1:] if ln.startswith("- ")]
        sections.append((date, entries))
    return intro, sections


def render_changelog(intro, sections):
    out = intro.rstrip("\n") + "\n"
    for date, entries in sections:
        out += f"## {date}\n"
        for entry in entries:
            out += entry + "\n"
        out += "\n"
    return out.rstrip("\n") + "\n"


def main():
    tracked = json.loads(TRACKED.read_text())
    repos = [r for r in tracked["repos"] if r.get("status", "active") == "active"]
    last_seen = json.loads(LAST_SEEN.read_text())

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    unreachable = []

    obs = {}
    changes = []
    for repo in repos:
        rid, owner, name = repo["id"], repo["owner"], repo["name"]
        ref = repo.get("ref", "HEAD")
        old = last_seen.get(rid)
        try:
            meta = repo_meta(owner, name)
            branch = meta["default_branch"] if ref == "HEAD" else ref
            sha, commit_date = repo_commit(owner, name, branch)
            version, version_url = repo_version(owner, name)
            blocks = {}
            for cat, path in repo.get("block_paths", {}).items():
                bsha, bdate = path_commit(owner, name, branch, path)
                if bsha:
                    blocks[cat] = {"sha": bsha, "date": bdate}
        except Exception as exc:  # keep the last known state, report it
            print(f"unreachable: {owner}/{name}: {exc}", file=sys.stderr)
            unreachable.append(rid)
            if not old:
                continue
            obs[rid] = old
            continue

        entry = dict(old) if old else {"sha": sha, "prev": None, "date": commit_date}
        if old and old["sha"] != sha:
            entry["prev"] = old["sha"]
            entry["date"] = commit_date
            changes.append(
                (commit_date, meta["pushed_at"], owner, name, old["sha"], sha)
            )
        entry["sha"] = sha
        entry["pushed_at"] = day(meta["pushed_at"]) or commit_date
        if version:
            entry["version"] = version
            entry["version_url"] = version_url
        else:
            entry.pop("version", None)
            entry.pop("version_url", None)
        if blocks:
            entry["blocks"] = blocks
        obs[rid] = entry

    # Persist last-seen keeping every existing key in place (the file's key order
    # is historic); new repos are appended after the last entry.
    new_last_seen = {}
    for key, value in last_seen.items():
        if key == "_unreachable":
            new_last_seen[key] = unreachable
        elif key == "_tracked_count":
            new_last_seen[key] = len(repos)
        elif key in obs:
            new_last_seen[key] = obs[key]
        else:
            new_last_seen[key] = value
    for rid, entry in obs.items():
        if rid not in new_last_seen:
            new_last_seen[rid] = entry
    LAST_SEEN.write_text(json.dumps(new_last_seen, indent=1, ensure_ascii=True) + "\n")

    readme_text = README.read_text()
    blocks = "\n\n".join(render_readme(readme_text, repos, obs, cat) for cat in tracked["categories"])
    readme_text = replace_marked(readme_text, "<!-- HUB-STATUS:BEGIN -->", "<!-- HUB-STATUS:END -->", blocks)
    footer = (
        f"_Hub status last refreshed: {now} — {len(repos)} tracked, {len(unreachable)} unreachable._"
    )
    readme_text = replace_marked(
        readme_text, "<!-- HUB-FOOTER:BEGIN -->", "<!-- HUB-FOOTER:END -->", footer, blank_before_end=False
    )
    README.write_text(readme_text)

    status_text = STATUS.read_text()
    status_text = re.sub(r"^_Updated .*?_$", f"_Updated {now}._", status_text, count=1, flags=re.M)
    table = render_status(repos, obs)
    head, sep, _ = status_text.partition("| repo | category |")
    STATUS.write_text(head + table + "\n")

    intro, sections = parse_changelog(CHANGELOG.read_text())
    changes.sort(key=lambda c: (c[0], c[1]))
    for date, _pushed, owner, name, prev, sha in changes:
        line = (
            f"- **{owner}/{name}** `{prev[:8]}` → `{sha[:8]}` "
            f"([compare](https://github.com/{owner}/{name}/compare/{prev}...{sha}))"
        )
        if any(line in entries for _, entries in sections):
            continue
        for i, (d, entries) in enumerate(sections):
            if d == date:
                entries.append(line)
                break
        else:
            pos = 0
            while pos < len(sections) and sections[pos][0] > date:
                pos += 1
            sections.insert(pos, [date, [line]])
    CHANGELOG.write_text(render_changelog(intro, sections))

    print(f"hub: {len(changes)} changed, {len(unreachable)} unreachable, {len(repos)} tracked")


if __name__ == "__main__":
    main()
