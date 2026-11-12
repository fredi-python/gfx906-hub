# MI50 / gfx906 Hub

Community hub for LLM serving on AMD **MI50 (gfx906 / CDNA1)**: what's moving in the
tracked forks, and the standing setup notes.

> Status rows below are **auto-updated nightly** — edit `repos/tracked.json`, not the table.

## Tracked repos

<!-- HUB-STATUS:BEGIN -->
### vllm

| repo | updated | head | drift |
|---|---|---|---|
| [curvedinf/int8-vllm](https://github.com/curvedinf/int8-vllm) | 2026-11-12 | `73a386c8` | [50 commits](https://github.com/curvedinf/int8-vllm/compare/ad1f166ba59acc4eec9fb7c608e944c976b793de...73a386c8fa8539d167a529718b3c4dacbf5e5ea8) |
| [Luce-Org/lucebox](https://github.com/Luce-Org/lucebox) | 2026-11-12 | `cbc6d7c2` | [6 commits](https://github.com/Luce-Org/lucebox/compare/a08825666baabb4fe5af9d75109552a6b25b1848...cbc6d7c27108e984599e22670564aae16e0e7eb4) |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 2026-11-12 | `a7933519` | [34 commits](https://github.com/vllm-project/vllm/compare/c6573eed5e56fd39b01d610db04616ed9b221851...a7933519764efd3b51782ebd7df4362c527e4a4c) |
| [ttdxq/gfx906-vllm](https://github.com/ttdxq/gfx906-vllm) | 2026-11-08 | `3eeb931d` | — |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906) | 2026-11-06 | `4c4fb1d2` | — |
| [KIntegrated/vllm-gfx906-mobydick](https://github.com/KIntegrated/vllm-gfx906-mobydick) | 2026-10-26 | `3857591d` | — |
| [0c33/mi50-vllm-lab](https://github.com/0c33/mi50-vllm-lab) | 2026-10-26 | `eb3b1728` | — |
| [cassettesgoboom/gfx906-fa-vllm](https://github.com/cassettesgoboom/gfx906-fa-vllm) | 2026-04-22 | `e0eb52a3` | — |
| [Lowkey-Loki-SN/noflash-attention](https://github.com/Lowkey-Loki-SN/noflash-attention) | 2026-03-28 | `8ffe5793` | — |

### strata

| repo | updated | head | drift |
|---|---|---|---|
| [ROCm/aiter](https://github.com/ROCm/aiter) | 2026-11-12 | `37da1dbe` | [12 commits](https://github.com/ROCm/aiter/compare/e9efac0e281410c5a0cf0bc5e8c6734feb8ce2f8...37da1dbeb305e868dda2e52d0d084a30fd71a99c) |
| [curvedinf/int8-aiter](https://github.com/curvedinf/int8-aiter) | 2026-11-12 | `cd53c11c` | [4 commits](https://github.com/curvedinf/int8-aiter/compare/2d5f5e0b55325f0799538550b2a63722092deac5...cd53c11c6d399cd79aee9500536dc5f8206f6ea3) |

### llamacpp

_(none tracked)_

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
_Hub status last refreshed: 2026-11-12 17:19 UTC — 12 tracked, 0 unreachable._
<!-- HUB-FOOTER:END -->
