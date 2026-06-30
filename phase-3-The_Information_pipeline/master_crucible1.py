import sys
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

filter = {
    "userId" : 7
}

try:
    response = requests.get(url,timeout=5,params=filter)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"Pipeline halted. Server returned an error: {e}")
    sys.exit()

post_data = response.json()

if(len(post_data) == 0):
    print("WARNING:no posts were found for that user.")

else:
    print(f"Total number of posts posted by user:{len(post_data)}")
    for x in post_data:
        print(f"Title:[{x['title']}]")
