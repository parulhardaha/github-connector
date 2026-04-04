from main import headers, requests, app


@app.get("/repos/{username}")
def get_repos(username: str):
    url = f"https://api.github.com/users/{username}/repos"
    # include headers so authenticated rate limits and access apply
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch repos"}

    return response.json()