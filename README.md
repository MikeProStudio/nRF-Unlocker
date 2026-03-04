# nRF-Unlocker 🔓

A lightweight Python tool to **erase and unlock** nRF54L and other ARM Cortex-M chips using low-cost **CMSIS-DAP** probes. No Segger J-Link license required.

## Why this tool?

When working with the **nRF54L series**, standard tools like OpenOCD or basic pyOCD commands often fail if the chip is locked (APPROTECT). You will typically see errors like:

> `Error: Failed to read memory at 0xe000ed00`  
> `Warn : target nrf54l.cpu examination failed`  
> `Error: [nrf54l.cpu] DP initialisation failed`

This happens because the chip blocks the debugger from reading system registers before the mass erase is completed. 

**nRF-Unlocker** solves this by:
1. Identifying the probe automatically.
2. Initiating a specialized `mass erase`.
3. **Automatic Retry:** It detects the communication fault caused by the unlock process and retries the connection after a short delay, ensuring a successful recovery.

### Features
- **Auto-Probe Detection**: Finds your debugger's Serial ID automatically.
- **Smart Retry**: Automatically handles communication faults during `APPROTECT` recovery.
- **Open Source**: Works with any CMSIS-DAP compatible adapter (e.g., Seeed Studio).

### Setup
1. Create environment: `python -m venv .venv`
2. 
- Windows: .\.venv\Scripts\Activate.ps1
- Linux/Mac: source .venv/bin/activate

3. Install: `pip install -r requirements.txt`

### Usage
`python erase.py --target nrf54l`