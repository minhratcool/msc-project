import requests
import json

# Define the endpoint URL
url = "http://127.0.0.1:5000/chat"

# Define the payload
payload = {
    "channel_id": 1,
    "user_email": "minh@google.com",
    "text": "I hate it!"
}

# Send 100 POST requests
for _ in range(500):
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Request successful")
    else:
        print(f"Request failed with status code: {response.status_code}")