# MI50 / gfx906 Hub

Community hub for LLM serving on AMD **MI50 (gfx906 / CDNA1)**: what's moving in the
tracked forks, and the standing setup notes.

> Status rows below are **auto-updated nightly** — edit `repos/tracked.json`, not the table.

## Tracked repos

<!-- HUB-STATUS:BEGIN -->
### vllm

| repo | updated | head | drift |
|---|---|---|---|
| [curvedinf/int8-vllm](https://github.com/curvedinf/int8-vllm) | 2026-11-12 | `971ed928` | [1 commits](https://github.com/curvedinf/int8-vllm/compare/03705db9fcefc9facd49929c005c0a4e5734c638...971ed9281347edb697313b07cc16fd13e670986c) |
| [Luce-Org/lucebox](https://github.com/Luce-Org/lucebox) | 2026-11-12 | `cbc6d7c2` | [6 commits](https://github.com/Luce-Org/lucebox/compare/a08825666baabb4fe5af9d75109552a6b25b1848...cbc6d7c27108e984599e22670564aae16e0e7eb4) |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 2026-11-12 | `c74cab9b` | [2 commits](https://github.com/vllm-project/vllm/compare/df5d80339b5fbca645e991444970b75fa330cd35...c74cab9b33659e92de9ca9c35eb949c78ebbe64c) |
| [ttdxq/gfx906-vllm](https://github.com/ttdxq/gfx906-vllm) | 2026-11-08 | `3eeb931d` | — |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906) | 2026-11-06 | `4c4fb1d2` | — |
| [KIntegrated/vllm-gfx906-mobydick](https://github.com/KIntegrated/vllm-gfx906-mobydick) | 2026-10-26 | `3857591d` | — |
| [0c33/mi50-vllm-lab](https://github.com/0c33/mi50-vllm-lab) | 2026-10-26 | `eb3b1728` | — |
| [ai-infos/vllm-gfx906-mobydick](https://github.com/ai-infos/vllm-gfx906-mobydick) | 2026-10-08 | `e7b96a5e` | — |
| [cassettesgoboom/gfx906-fa-vllm](https://github.com/cassettesgoboom/gfx906-fa-vllm) | 2026-04-22 | `e0eb52a3` | — |
| [Lowkey-Loki-SN/noflash-attention](https://github.com/Lowkey-Loki-SN/noflash-attention) | 2026-03-28 | `8ffe5793` | — |

### strata

| repo | updated | head | drift |
|---|---|---|---|
| [ROCm/aiter](https://github.com/ROCm/aiter) | 2026-11-12 | `27f774a9` | [1 commits](https://github.com/ROCm/aiter/compare/04df8dd468d2563e035db254e94d6ad1781e311d...27f774a92f02467fa99f707139d26abf81e8f37a) |
| [curvedinf/int8-aiter](https://github.com/curvedinf/int8-aiter) | 2026-11-12 | `b5efe248` | [1 commits](https://github.com/curvedinf/int8-aiter/compare/cd53c11c6d399cd79aee9500536dc5f8206f6ea3...b5efe248dfc62993ff93bfafed3f6946cac7c653) |

### llamacpp

| repo | updated | head | drift |
|---|---|---|---|
| [mxxm-t/mx-llama.cpp](https://github.com/mxxm-t/mx-llama.cpp) | 2026-11-06 | `cdc81dae` | — |

### other

| repo | updated | head | drift |
|---|---|---|---|
| [joe2gaan/localaiservers](https://github.com/joe2gaan/localaiservers) | 2026-07-01 | `3502012d` | — |

<!-- HUB-STATUS:END -->

## Common info

### PCIe P2P on MI50
Full-BAR / `CONFIG_PCI_P2PDMA` P2P on MI50 boxes — the runbook. **Setup guide incoming
(link TBA).**

### MI50 "Catch Me If You Can" leaderboard
The public single-stream decode challenge for the MI50 (r/LocalAIServers):
https://www.reddit.com/r/LocalAIServers/comments/1ukhr24/

## Change log

[CHANGELOG.md](CHANGELOG.md) — every nightly drift, newest first.

<!-- HUB-FOOTER:BEGIN -->
_Hub status last refreshed: 2026-11-12 19:47 UTC — 14 tracked, 0 unreachable._
<!-- HUB-FOOTER:END -->
