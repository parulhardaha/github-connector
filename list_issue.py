from main import headers, requests, app
@app.get("/issues/{owner}/{repo}")
def list_issues(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch issues"}

    return response.json()