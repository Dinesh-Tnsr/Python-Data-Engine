import requests

# This endpoint is hardcoded by the server to delay its response by 5 seconds
slow_url = "https://httpbin.org/delay/5"
bad_url = "https://httpbin.org/status/404"

print("--- Defensive Network Engine Online ---")

try:
    print("Attempting connection to slow server...")
    requests.get(slow_url,timeout=3)
    print("Connection Successfull")

except requests.exceptions.Timeout:
    print("CRITICAL: Server timed out. Aborting connection.")


try:
    print("Attempting connection to bad server...")
    response = requests.get(bad_url, timeout=3)
    response.raise_for_status()
    print("Data downloaded")

except requests.exceptions.RequestException as e:
    print(f"Pipeline halted. Server returned an error: {e}")