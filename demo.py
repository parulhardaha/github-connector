import requests

url = "https://api.github.com/repos/parulhardaha/URL-Shortner/issues"

headers = {
    "Authorization": "token YOUR_GITHUB_TOKEN"
}

data = {
    "title": "Bug in login",
    "body": "Login page not working..."
}

requests.post(url, json=data, headers=headers)