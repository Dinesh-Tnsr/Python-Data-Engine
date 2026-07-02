import sys
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
print(f"Target locked: {url}")
print("-" * 50)

try:
    response = requests.get(url,timeout=5)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"Pipeline halted. Server returned an error: {e}")
    sys.exit()

user_json = response.json()
user_df = pd.DataFrame(user_json)

print(user_df.head(3))
print(user_df.info())