import requests

# The Target Endpoint
url = "https://jsonplaceholder.typicode.com/users/1"
print(f"Target locked: {url}")
print("-" * 50)

response = requests.get(url)

print(response.status_code)
print(response.headers['Content-Type'])
print(response.text)
