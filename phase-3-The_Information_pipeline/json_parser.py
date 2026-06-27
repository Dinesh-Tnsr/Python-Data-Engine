import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    print("Connection Established. Decoding payload...")

    users_data = response.json()
    print(type(users_data))
    print(len(users_data))
    user = users_data[0]
    print(f"Target User: [{user['name']}]")

    print(f"Target City:[{user['address']['city']}]")
else:
    print(f"Network Failure: {response.status_code}")

