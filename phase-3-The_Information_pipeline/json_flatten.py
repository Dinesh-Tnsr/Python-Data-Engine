import sys
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
print(f"Target locked: {url}")
print("-" * 50)

try:
    response = requests.get(url,timeout=5)
    response.raise_for_status()

    users_json = response.json()

    flat_df = pd.json_normalize(users_json)

    print(flat_df.info())

    mask = flat_df["address.city"] == "Gwenborough"

    print(flat_df[mask])



except requests.exceptions.RequestException as e:
    print(f"Pipeline halted. Server returned an error: {e}")
    sys.exit()

