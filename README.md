# nRF-Unlocker 🔓

A lightweight Python tool to **erase and unlock** nRF54L and other ARM Cortex-M chips using low-cost **CMSIS-DAP** probes. No Segger J-Link license required.

### Features
- **Auto-Probe Detection**: Finds your debugger's Serial ID automatically.
- **Smart Retry**: Automatically handles communication faults during `APPROTECT` recovery.
- **Open Source**: Works with any CMSIS-DAP compatible adapter (e.g., Seeed Studio).

### Setup
1. Create environment: `python -m venv .venv`
2. Activate: `.\.venv\Scripts\Activate.ps1`
3. Install: `pip install -r requirements.txt`

### Usage
`python erase.py --target nrf54l`