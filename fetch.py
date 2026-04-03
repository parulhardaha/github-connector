from main import   headers, requests, app, GITHUB_TOKEN  
@app.get("/repos/{username}")
def get_repos(username: str):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch repos"}

    return response.json()