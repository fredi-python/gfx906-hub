# MI50 / gfx906 Hub

Community hub for LLM serving on AMD **MI50 (gfx906 — Vega 20)**: what's moving in the
tracked forks, and the standing setup notes.

> Status rows below are **auto-updated nightly** — edit `repos/tracked.json`, not the table.

## Tracked repos

<!-- HUB-STATUS:BEGIN -->
### vllm

| repo | updated | head | version | drift |
|---|---|---|---|---|
| [ttdxq/gfx906-vllm](https://github.com/ttdxq/gfx906-vllm) | 2026-11-08 | `3eeb931d` | [rccl-gfx906-2.27.7-rocm7.2.4](https://github.com/ttdxq/gfx906-vllm/releases/tag/rccl-gfx906-2.27.7-rocm7.2.4) | — |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906) · [vllm](https://github.com/mixa3607/ML-gfx906/blob/master/vllm-v2/README.md) · [llama.cpp](https://github.com/mixa3607/ML-gfx906/blob/master/llama.cpp/README.md) · [llama.cpp multiruntime](https://github.com/mixa3607/ML-gfx906/blob/master/llama.cpp-multiruntime/README.md) · [comfyui](https://github.com/mixa3607/ML-gfx906/blob/master/comfyui/README.md) · [pytorch](https://github.com/mixa3607/ML-gfx906/blob/master/pytorch/README.md) · [rocm](https://github.com/mixa3607/ML-gfx906/blob/master/rocm/README.md) · [strata](https://github.com/mixa3607/ML-gfx906/blob/master/strata/README.md) · [project-maya](https://github.com/mixa3607/ML-gfx906/blob/master/project-maya/README.md) | 2026-11-06 | `4c4fb1d2` | [20261031203345](https://github.com/mixa3607/ML-gfx906/releases/tag/20261031203345) | — |
| [KIntegrated/vllm-gfx906-mobydick](https://github.com/KIntegrated/vllm-gfx906-mobydick) | 2026-10-26 | `3857591d` | gfx906/v0.31.0-final | — |
| [0c33/mi50-vllm-lab](https://github.com/0c33/mi50-vllm-lab) | 2026-10-26 | `eb3b1728` | — | — |
| [ai-infos/vllm-gfx906-mobydick](https://github.com/ai-infos/vllm-gfx906-mobydick) | 2026-10-08 | `e7b96a5e` | — | — |
| [joe2gaan/localaiservers](https://github.com/joe2gaan/localaiservers) | 2026-07-01 | `3502012d` | [vnext-gfx906-rocm72-gguf-hf-repro](https://github.com/joe2gaan/localaiservers/releases/tag/vnext-gfx906-rocm72-gguf-hf-repro) | — |
| [cassettesgoboom/gfx906-fa-vllm](https://github.com/cassettesgoboom/gfx906-fa-vllm) | 2026-04-22 | `e0eb52a3` | — | — |

### llamacpp

| repo | updated | head | version | drift |
|---|---|---|---|---|
| [mxxm-t/mx-llama.cpp](https://github.com/mxxm-t/mx-llama.cpp) | 2026-11-06 | `cdc81dae` | b11757 | — |

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
_Hub status last refreshed: 2026-11-13 03:05 UTC — 8 tracked, 0 unreachable._
<!-- HUB-FOOTER:END -->
