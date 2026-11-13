# MI50 / gfx906 Hub

Community hub for LLM serving on AMD **MI50 (gfx906 — Vega 20)**: what's moving in the
tracked forks, and the standing setup notes.

> Status rows below are **auto-updated nightly**.

## Tracked repos

<!-- HUB-STATUS:BEGIN -->
### vllm

| repo | updated | head | version | drift |
|---|---|---|---|---|
| [ttdxq/gfx906-vllm](https://github.com/ttdxq/gfx906-vllm) | 2026-11-08 | `3eeb931d` | [rccl-gfx906-2.27.7-rocm7.2.4](https://github.com/ttdxq/gfx906-vllm/releases/tag/rccl-gfx906-2.27.7-rocm7.2.4) | — |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906/blob/master/vllm-v2/README.md) | 2026-11-06 | `4c4fb1d2` | [20261031203345](https://github.com/mixa3607/ML-gfx906/releases/tag/20261031203345) | — |
| [KIntegrated/vllm-gfx906-mobydick](https://github.com/KIntegrated/vllm-gfx906-mobydick) | 2026-10-26 | `3857591d` | gfx906/v0.31.0-final | — |
| [0c33/mi50-vllm-lab](https://github.com/0c33/mi50-vllm-lab) | 2026-10-26 | `eb3b1728` | — | — |
| [joochung/vllm-gfx906-mobydick](https://github.com/joochung/vllm-gfx906-mobydick) | 2026-10-17 | `524ac6f2` | v0.30-first-good-boot | — |
| [ai-infos/vllm-gfx906-mobydick](https://github.com/ai-infos/vllm-gfx906-mobydick) | 2026-10-08 | `e7b96a5e` | — | — |
| [phantomic12/ML-gfx906](https://github.com/phantomic12/ML-gfx906) | 2026-08-16 | `e816905b` | [20260802001858](https://github.com/phantomic12/ML-gfx906/releases/tag/20260802001858) | — |
| [joe2gaan/localaiservers](https://github.com/joe2gaan/localaiservers) | 2026-07-01 | `3502012d` | [vnext-gfx906-rocm72-gguf-hf-repro](https://github.com/joe2gaan/localaiservers/releases/tag/vnext-gfx906-rocm72-gguf-hf-repro) | — |
| [cassettesgoboom/gfx906-fa-vllm](https://github.com/cassettesgoboom/gfx906-fa-vllm) | 2026-04-22 | `e0eb52a3` | — | — |

### llamacpp

| repo | updated | head | version | drift |
|---|---|---|---|---|
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906/blob/master/llama.cpp/README.md) | 2026-11-06 | `4c4fb1d2` | [20261031203345](https://github.com/mixa3607/ML-gfx906/releases/tag/20261031203345) | — |
| [mxxm-t/mx-llama.cpp](https://github.com/mxxm-t/mx-llama.cpp) | 2026-11-06 | `cdc81dae` | b11757 | — |
| [anng-phtk/rocm-vega-llama.cpp](https://github.com/anng-phtk/rocm-vega-llama.cpp) | 2026-08-25 | `602a7b55` | — | — |

### strata

| repo | updated | head | version | drift |
|---|---|---|---|---|
| [hboyd2003/Strata](https://github.com/hboyd2003/Strata) | 2026-11-12 | `3b54d622` | [v0.2.13+0.5-gfx906](https://github.com/hboyd2003/Strata/releases/tag/v0.2.13%2B0.5-gfx906) | — |
| [mixa3607/ML-gfx906](https://github.com/mixa3607/ML-gfx906/blob/master/strata/README.md) | 2026-11-06 | `4c4fb1d2` | [20261031203345](https://github.com/mixa3607/ML-gfx906/releases/tag/20261031203345) | — |

<!-- HUB-STATUS:END -->

## Common info

### PCIe P2P on MI50

Runbook for getting P2P working across 32GB MI50s — VBIOS check, BAR limits, GRUB +
BIOS settings, RCCL env, and how to confirm it's actually P2P.
Source: [community guide (pastebin)](https://pastebin.com/raw/g9hFc9WZ)

**1. VBIOS check** — you need a PCIE P2P VBIOS; only these are supported:

```bash
vbios_list=$(rocm-smi --showvbios | grep -oP 'VBIOS version: \K[0-9A-Za-z-]+'); supported=("113-D1631700-111" "113-D1640200-043" "113-D163A1XT-045"); fail=0; echo "Checking VBIOS for P2P/ReBAR support..."; for v in $vbios_list; do if [[ " ${supported[@]} " =~ " $v " ]]; then echo "  ✅ $v : Supported"; else echo "  ❌ $v : Unsupported (P2P will fail)"; fail=1; fi; done; [ $fail -eq 0 ] && echo "Success: All GPUs have supported VBIOS" || echo "Error: Flash unsupported GPUs to MI50/V420 ROMs"
```

If you don't have one, flash per this guide:
https://gist.github.com/evilJazz/14a4c82a67f2c52a6bb5f9cea02f5e13

**2. Root complex check** — tells you if your GPUs are on the same root complex.
P2P *should* work across nodes and switches, but the latency benefits will be greatly reduced:

```bash
rcs=$(for dev in $(lspci -D | grep -i "MI50\|Vega 20" | awk '{print $1}'); do readlink -f /sys/bus/pci/devices/$dev | grep -oE 'pci0000:[0-9a]+' | head -1; done | sort -u); n=$(echo $rcs | wc -w); echo "Root complexes: $rcs"; [ $n -eq 1 ] && echo "All GPUs on same root complex" || echo "GPUs on DIFFERENT root complexes"
```

**3. BAR check (16TB / 44-bit limit)** — if any are over the limit, lower the MMIO Base in BIOS (step 5):

```bash
devs=$(lspci -D | grep -i "MI50\|Vega 20" | awk '{print $1}'); fail=0; echo "Checking GPU BARs (16TB / 44-bit limit = 0x100000000000):"; for d in $devs; do addrs=$(lspci -s $d -v | grep "Memory at" | awk '{print $3}'); for a in $addrs; do if [ $((16#$a)) -ge $((16#100000000000)) ]; then echo "$d  0x$a : OVER LIMIT - P2P WILL FAIL!"; fail=1; else echo "$d  0x$a : SAFE"; fi; done; done; [ $fail -eq 0 ] && echo "SUCCESS: All GPU memory addresses are safely mapped below 16TB." || echo "ERROR: Memory mapping exceeds the Vega 20 limit. Lower MMIO Base in BIOS!"
```

**4. GRUB** — before rebooting, edit `/etc/default/grub` (use `amd_iommu=on` if on AMD):

```text
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash intel_iommu=on iommu=pt pcie_acs_override=downstream,multifunction"
```

- AMD's docs say not to use `iommu=pt`, but on the guide author's Intel X99 platform it
  deadlocks during NCCL init without it.
- `pcie_acs_override=downstream,multifunction` was required for P2P on the author's
  PLX switch. Shouldn't hurt to add it anyways.

Then `sudo update-grub` and `sudo poweroff`.

**5. BIOS** — find MMIO Base / MMIO High (one will be "G" for gigabytes, one "T" for terabytes):

- MMIO Base (T): `1T` or `2T`
- MMIO High (G): `256G`

Along with the MMIO settings, make sure these are set:

- ReBAR / Above 4G Decoding: `Enabled`
- IOMMU / Intel VT-d: `Enabled`
- ACS (Access Control Services): `Disabled` (if visible)
- ASPM: `Disabled`
- SR-IOV: `Disabled`

*(Note: AMD platforms will have different options. This may require a BIOS update or
custom BIOS — try searching the web with your motherboard model and "MMIO" if you can't
locate the settings.)*

**6. Verify the driver sees the links** — needs to be `True` across the board:

```bash
rocm-smi --showtopoaccess
```

**7. Run vLLM with these env vars:**

```yaml
      -e NCCL_DEBUG=INFO
      -e NCCL_P2P_LEVEL=PXB(same PCI root) PIX(active PCI switch) SYS (anywhere)
      -e RCCL_P2P_DISABLE=0
      -e VLLM_SKIP_P2P_CHECK=1
      -e HSA_FORCE_FINE_GRAIN_PCIE=1
      -e HSA_OVERRIDE_GFX_VERSION=9.0.6
      -e ROCR_VISIBLE_DEVICES=0,1,2,3
```

e.g. `aiinfos/vllm-gfx906-mobydick:latest` → `vllm serve <model> --disable-custom-all-reduce`.
If using >2 GPUs, `--disable-custom-all-reduce` is needed to force RCCL over vLLM's
default all-reduce (shouldn't hurt to use it with TP2).

**8. Confirm it's actually P2P** — check your logs:

```bash
docker logs vllm 2>&1 | grep -i "via"
```

- ✅ Success (P2P working): `NCCL INFO Channel 00 : 0[7000] -> 1[d000] via P2P/IPC comm...`
- ❌ Failure (fell back to system RAM): `NCCL INFO Channel 00 : 0[7000] -> 1[d000] via SHM/direct/direct comm...`

**Troubleshooting:**

Check PCIe ASPM along the MI50 paths (want Disabled / Not supported):

```bash
echo "Tracing MI50 PCIe paths and checking ASPM..."; for gpu in $(lspci -D -d 1002:66a1 | awk '{print $1}'); do cur=$gpu; while [ -n "$cur" ] && [[ ! "$cur" =~ pci0000 ]]; do name=$(lspci -s $cur | cut -d' ' -f2-); aspm=$(sudo lspci -vvv -s $cur | grep "ASPM" | grep "LnkCtl:" | grep -oE "ASPM (Disabled|L0s|L1|L0s L1)"); [ -z "$aspm" ] && aspm="Not supported"; if [[ "$aspm" == *"Disabled"* ]] || [[ "$aspm" == *"Not supported"* ]]; then echo "  ✅ $cur ($name) : $aspm"; else echo "  ❌ $cur ($name) : $aspm (Disable in BIOS/GRUB)"; fi; parent=$(readlink -f /sys/bus/pci/devices/$cur/.. 2>/dev/null); cur=$(basename "$parent"); done; done
```

Try forcing high performance: `sudo rocm-smi --setperflevel high`

### MI50 "Catch Me If You Can" leaderboard
The public single-stream decode challenge for the MI50 (r/LocalAIServers):
https://www.reddit.com/r/LocalAIServers/comments/1ukhr24/

## Change log

[CHANGELOG.md](CHANGELOG.md) — every nightly drift, newest first.

<!-- HUB-FOOTER:BEGIN -->
_Hub status last refreshed: 2026-11-13 15:08 UTC — 12 tracked, 0 unreachable._
<!-- HUB-FOOTER:END -->
