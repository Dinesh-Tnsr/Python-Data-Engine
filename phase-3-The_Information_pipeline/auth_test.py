import requests

# The secure endpoint
url = "https://httpbin.org/bearer"

# simulated API token
my_api_key = "ENG_TOKEN_9948X_ALPHA"

print(f"Target locked: {url}")
print("-" * 50)

rejected_response = requests.get(url)
print(rejected_response.status_code)

secure_header = {
    "Authorization" : f"Bearer {my_api_key}" 
}

approved_response = requests.get(url,headers=secure_header)

print(approved_response.status_code)
print(approved_response.json())