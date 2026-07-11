import sys
import requests
import html
import time
import pandas as pd

url = "https://jsonplaceholder.typicode.com/comments"
print("--- Live Analytics Engine Online ---")

master_list = []
count_pages = 1

while(9):
    filter = {
        "_page" : count_pages,
        "_limit" : 100
    }
    try:
        response = requests.get(url,timeout=5,params=filter)
        response.raise_for_status()

        page_data = response.json()

        if(len(page_data) == 0):
            print("Scrape complete")
            break
        else:
            print(f"scrapped page:{count_pages}")
            master_list.extend(page_data)
            count_pages = count_pages+1
            print("slow downing the API calls for a second due to rapid API calls")
            time.sleep(1)



    except requests.exceptions.RequestException as e:
        print(f"system halted! server returned an error:{e}")
        sys.exit()


print(pd.DataFrame(master_list).info())

clean_data = []

for record in master_list:
    clear_data = {
        "postId" : record["postId"],
        "id" : record["id"],
        "email" : record["email"],
        "body" : html.unescape(record.get("body","No Text")).replace("\n","").strip()
    }
    clean_data.append(clear_data)

df = pd.DataFrame(clean_data)
print(df.info())

comments_count = df.groupby("postId")["id"].count()

print(comments_count.head(5))

