import sys
import subprocess
import re
import time

def execute_pyocd_erase(probe_id, target="nrf54l"):
    erase_cmd = [
        sys.executable, "-m", "pyocd", "erase", 
        "-u", probe_id, 
        "-t", target, 
        "--mass", "-v"
    ]
    return subprocess.run(erase_cmd, check=True)

def run_erase():
    print("--- Scanning for connected debug probes ---")
    try:
        result = subprocess.run([sys.executable, "-m", "pyocd", "list"], capture_output=True, text=True)
        match = re.search(r"([A-F0-9]{8,})", result.stdout)
        
        if not match:
            print("Error: No probe detected. Check connection/drivers.")
            return

        probe_id = match.group(1)
        print(f"--- Found Probe: {probe_id} ---")
        max_attempts = 2
        for attempt in range(1, max_attempts + 1):
            try:
                print(f"--- Attempt {attempt} of {max_attempts}: Starting Mass Erase ---")
                execute_pyocd_erase(probe_id)
                print("--- Success: Device erased and unlocked! ---")
                break
            
            except subprocess.CalledProcessError:
                if attempt < max_attempts:
                    print("\n[!] Communication failure (likely due to APPROTECT unlock).")
                    print("[!] Resetting connection and retrying in 2 seconds...\n")
                    time.sleep(2)
                else:
                    print("\n[!] Error: Mass erase failed after 2 attempts.")
                    print("[!] Please check your wiring and power supply.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_erase()