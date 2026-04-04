import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

url = "https://api.github.com/repos/parulhardaha/Flaskify-API/issues"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

data = {
    "title": "Bug in login",
    "body": "Login page not working..."
}

#print("TOKEN:", os.getenv("GITHUB_TOKEN"))

response = requests.post(url, json=data, headers=headers)

print("Status:", response.status_code)
print("Response:", response.text)