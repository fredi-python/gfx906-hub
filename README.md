# MI50 / gfx906 Hub

Community hub for LLM serving on AMD **MI50 (gfx906 — Vega 20)**: what's moving in the
tracked forks, and the standing setup notes.

> Status rows below are **auto-updated nightly**.

## Tracked repos

<!-- HUB-STATUS:BEGIN -->
### vllm

| repo | focus | updated | head | version |
|---|---|---|---|---|
| [ttdxq/gfx906-vllm](https://github.com/ttdxq/gfx906-vllm) | open kernel-source fork (GDN decode stack) + RCCL gfx906 builds | 2026-11-08 | `3eeb931d` | [rccl-gfx906-2.27.7-rocm7.2.4](https://github.com/ttdxq/gfx906-vllm/releases/tag/rccl-gfx906-2.27.7-rocm7.2.4) |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906/blob/master/vllm-v2/README.md) | the base monorepo — vllm, llama.cpp, strata (+ more) for gfx906 | 2026-11-06 | `4c4fb1d2` | [20261031203345](https://github.com/mixa3607/ML-gfx906/releases/tag/20261031203345) |
| [KIntegrated/vllm-gfx906-mobydick](https://github.com/KIntegrated/vllm-gfx906-mobydick) | newest vLLM base (v0.31 line) — current release gfx906/v0.31.0-final | 2026-10-26 | `3857591d` | gfx906/v0.31.0-final |
| [0c33/mi50-vllm-lab](https://github.com/0c33/mi50-vllm-lab) | 27B on 2× MI50 — gfx906_skinny 4-bit kernels (lab / experiments) | 2026-10-26 | `eb3b1728` | — |
| [joochung/vllm-gfx906-mobydick](https://github.com/joochung/vllm-gfx906-mobydick) | PLE CPU-offload — big MoE models on 16GB cards (v0.30 line) | 2026-10-17 | `524ac6f2` | v0.30-first-good-boot |
| [ai-infos/vllm-gfx906-mobydick](https://github.com/ai-infos/vllm-gfx906-mobydick) | multi-GPU / TP4 serving (the 4×MI50 P2P guide runs on this image) | 2026-10-08 | `e7b96a5e` | — |
| [phantomic12/ML-gfx906](https://github.com/phantomic12/ML-gfx906) | mixa monorepo fork (dormant) — GitHub-hosted apt-repo build POC | 2026-08-16 | `e816905b` | [20260802001858](https://github.com/phantomic12/ML-gfx906/releases/tag/20260802001858) |
| [joe2gaan/localaiservers](https://github.com/joe2gaan/localaiservers) | vNext vLLM — closed .so runtime overlay, dense + MoE profiles, bench reports | 2026-07-01 | `3502012d` | [vnext-gfx906-rocm72-gguf-hf-repro](https://github.com/joe2gaan/localaiservers/releases/tag/vnext-gfx906-rocm72-gguf-hf-repro) |
| [cassettesgoboom/gfx906-fa-vllm](https://github.com/cassettesgoboom/gfx906-fa-vllm) | flash-attention kernels for gfx906 (feeds the gfx906_fa vLLM backend) | 2026-04-22 | `e0eb52a3` | — |

### llamacpp

| repo | focus | updated | head | version |
|---|---|---|---|---|
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906/blob/master/llama.cpp/README.md) | the base monorepo — vllm, llama.cpp, strata (+ more) for gfx906 | 2026-11-06 | `4c4fb1d2` | [20261031203345](https://github.com/mixa3607/ML-gfx906/releases/tag/20261031203345) |
| [mxxm-t/mx-llama.cpp](https://github.com/mxxm-t/mx-llama.cpp) | llama.cpp mx builds — Qwen3 / 3.5 GGUF quants (Q8 to Q4) on 16GB | 2026-11-06 | `cdc81dae` | b11757 |
| [anng-phtk/rocm-vega-llama.cpp](https://github.com/anng-phtk/rocm-vega-llama.cpp) | mixed-GPU llama.cpp (Vega 64 + MI50) on ROCm 7.2 | 2026-08-25 | `602a7b55` | — |

### strata

| repo | focus | updated | head | version |
|---|---|---|---|---|
| [hboyd2003/Strata](https://github.com/hboyd2003/Strata) | Strata tuned for gfx906 — rocBLAS autotune, prompt-attention env (~+7% prefill) | 2026-11-12 | `3b54d622` | [v0.2.13+0.5-gfx906](https://github.com/hboyd2003/Strata/releases/tag/v0.2.13%2B0.5-gfx906) |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906/blob/master/strata/README.md) | the base monorepo — vllm, llama.cpp, strata (+ more) for gfx906 | 2026-11-06 | `4c4fb1d2` | [20261031203345](https://github.com/mixa3607/ML-gfx906/releases/tag/20261031203345) |

<!-- HUB-STATUS:END -->

## Common info

### P2P Guide

Tips for getting P2P working on 32GB MI50s: [P2P setup guide](https://pastebin.com/raw/g9hFc9WZ)
— community runbook (VBIOS / BAR checks, GRUB + BIOS settings, RCCL env, verification).

## Change log

[CHANGELOG.md](CHANGELOG.md) — every repo move, newest first.

<!-- HUB-FOOTER:BEGIN -->
_Hub status last refreshed: 2026-11-13 17:36 UTC — 12 tracked, 0 unreachable._
<!-- HUB-FOOTER:END -->
