import sys
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/comments"
print("--- Live Analytics Engine Online ---")

try:
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    raw_data = response.json()

    df = pd.DataFrame(raw_data)
    comments_count = df.groupby("postId")["id"].count()
    print(comments_count)

except requests.exceptions.RequestException as e:
    print(f"pipeline halted! server returned an error:{e}")
    sys.exit()