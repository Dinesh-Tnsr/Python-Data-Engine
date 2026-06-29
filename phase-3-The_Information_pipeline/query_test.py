import requests

# The Master Database Endpoint (500 comments total)
url = "https://jsonplaceholder.typicode.com/comments"

print(f"Target locked: {url}")
print("-" * 50)

query_filters = {
    "postId" : 3
}

response = requests.get(url,params = query_filters)

print(response.url)
if (response.status_code == 200):
    data = response.json()
    print(len(data))
