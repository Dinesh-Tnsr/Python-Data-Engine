import sys
import time       
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
print("--- Defensively Paced Paginator Online ---")

master_data = []
current_page = 1

while(100):
    filter = {
        "_page" : current_page,
        "_limit" : 10
    }

    try:
        response = requests.get(url,timeout=5,params=filter)
        response.raise_for_status()
        page_data = response.json()

        if(len(page_data) == 0):
            print("End of document reached.")
            break
        else:
            print(f"scrapped page{current_page}")
            master_data.extend(page_data)
            current_page = current_page+1
            print("Throttling CPU for 1 second to respect API limits...")
            time.sleep(1)


    except requests.exceptions.RequestException as e:
        print(f"Pipeline halted. Server returned an error: {e}")
        sys.exit()


flat_df = pd.json_normalize(master_data)
print(flat_df.info())