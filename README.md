# MI50 / gfx906 Hub

Community hub for LLM serving on AMD **MI50 (gfx906 / CDNA1)**: what's moving in the
tracked forks, and the standing setup notes.

> Status rows below are **auto-updated nightly** — edit `repos/tracked.json`, not the table.

## Tracked repos

<!-- HUB-STATUS:BEGIN -->
| repo | role | status | last seen | updated | compare |
|---|---|---|---|---|---|
| [cassettesgoboom/gfx906-fa-vllm](https://github.com/cassettesgoboom/gfx906-fa-vllm) | gfx906 flash-attention kernels for vLLM (upstream of the gfx906_fa backend) | active | `e0eb52a3` | 2026-11-12 | - |
| [curvedinf/int8-vllm](https://github.com/curvedinf/int8-vllm) | int8 vLLM for gfx906 (dot4 lineage) | active | `ad1f166b` | 2026-11-12 | - |
| [curvedinf/int8-aiter](https://github.com/curvedinf/int8-aiter) | int8 AITER kernels for gfx906 | active | `2d5f5e0b` | 2026-11-12 | - |
| [Luce-Org/lucebox](https://github.com/Luce-Org/lucebox) | dflash / PFlash optimization lane (Qwen 3.8 Flash-Next) | active | `a0882566` | 2026-11-12 | - |
| [KIntegrated/vllm-gfx906-mobydick](https://github.com/KIntegrated/vllm-gfx906-mobydick) | gfx906 vLLM fork (mobydick) | active | `3857591d` | 2026-11-12 | - |
| [0c33/mi50-vllm-lab](https://github.com/0c33/mi50-vllm-lab) | MI50 vLLM lab — 27B on 2x MI50, gfx906_skinny 4-bit kernels | active | `eb3b1728` | 2026-11-12 | - |
| [ROCm/aiter](https://github.com/ROCm/aiter) | AMD AITER — reference for gfx906 gaps (CDNA3+ paths) | watch | `e9efac0e` | 2026-11-12 | [diff](https://github.com/ROCm/aiter/compare/6a80ddd9d23f3d76b4ce6b9b69f9d92073045bb5...e9efac0e281410c5a0cf0bc5e8c6734feb8ce2f8) |
| [joe2gaan/localaiservers](https://github.com/joe2gaan/localaiservers) | gfx906 compute site: deploy scripts, bench reports, closed .so overlays (vNext) | active | `3502012d` | 2026-11-12 | - |
| [ttdxq/gfx906-vllm](https://github.com/ttdxq/gfx906-vllm) | open .cu gfx906 vLLM fork (GDN decode stack) | active | `3eeb931d` | 2026-11-12 | - |
| [btbtyler09/vllm-gfx908](https://github.com/btbtyler09/vllm-gfx908) | MI100/gfx908 vLLM fork — reference only | reference | `745883c4` | 2026-11-12 | - |
| [larkinwc/vllm-gfx908](https://github.com/larkinwc/vllm-gfx908) | older MI100 vLLM fork — reference only | reference | `42d53e58` | 2026-11-12 | - |
| [Lowkey-Loki-SN/noflash-attention](https://github.com/Lowkey-Loki-SN/noflash-attention) | no-flash attention experiments for gfx906 | active | `8ffe5793` | 2026-11-12 | - |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906) | gfx906 ML base (upstream of the cassettesgoboom FA work) | active | `4c4fb1d2` | 2026-11-12 | - |
| [leapdragon/vllm-rdna2-qwen](https://github.com/leapdragon/vllm-rdna2-qwen/tree/rdna2/qwen38-flash-next) | RDNA2 4x32GB Qwen3.8-Flash-Next port (docs lane) | watch | `160184aa` | 2026-11-12 | - |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | mainline vLLM — gfx906 support is landing here upstream | active | `c6573eed` | 2026-11-12 | [diff](https://github.com/vllm-project/vllm/compare/52373885168d70886d0a047477a33f65f06b5dc0...c6573eed5e56fd39b01d610db04616ed9b221851) |
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
_Hub status last refreshed: 2026-11-12 08:10 UTC — 15 tracked, 0 unreachable._
<!-- HUB-FOOTER:END -->
