from main import headers, requests, app
@app.post("/create-issue/")
def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 201:
        return {"error": "Issue not created"}

    return response.json()