## Description
This project is a simple FastAPI application that interacts with the GitHub API. It allows users to fetch repository details, list all issues of a repository, and create new issues using API endpoints.

##
1. Shows repository details fetched from GitHub using owner and repo name.
<img width="901" height="882" alt="Screenshot 2026-04-04 at 2 53 43 PM" src="https://github.com/user-attachments/assets/094bf1e5-0f8f-4440-8cb8-2b007203f7e9" />

##
2. Displays all issues of a selected GitHub repository.
<img width="676" height="871" alt="Screenshot 2026-04-04 at 4 54 55 PM" src="https://github.com/user-attachments/assets/4a4a0a33-d43c-47c2-ad7a-80fb8f0aa243" />

##
3.Creates a new issue in the repository using title and body.
<img width="665" height="774" alt="creayed issue" src="https://github.com/user-attachments/assets/eaf1bab6-973a-418d-a22f-cff41390c6ba" />


## Demo Video
https://drive.google.com/file/d/1Hb2YNcyojpmM_0HMOtyWs3zsf64UtHHa/view?usp=sharing
## Setup

1. Clone the repository (if not already):

   ```bash
   git clone <repo-url>
   cd github-connector
   ```

2. Create and activate a virtual environment (macOS / zsh shown). This project uses a local `.venv` by convention:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your GitHub token:

   ```text
   GITHUB_TOKEN=ghp_...your_token_here...
   ```

   Note: Use a personal access token with `repo` scope to create issues on private repositories. For public-only operations, a token is optional but recommended to increase rate limits.

## How to run

Run the FastAPI app with uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## API endpoints

Base URL: `http://127.0.0.1:8000`

1. GET `/` — Home

   Returns a simple message.

   Example:
   ```bash
   curl http://127.0.0.1:8000/
   ```

2. GET `/repos/{username}` — List a user's repositories

   Path parameters:
   - `username` — GitHub username to fetch repos for.

   Example:
   ```bash
   curl http://127.0.0.1:8000/repos/parulhardaha
   ```

3. GET `/issues/{owner}/{repo}` — List issues in a repository

   Path parameters:
   - `owner` — repository owner (user or org)
   - `repo` — repository name

   Example:
   ```bash
   curl http://127.0.0.1:8000/issues/parulhardaha/my-repo
   ```

4. POST `/create-issue/` — Create a new issue

   Current implementation expects these parameters as query parameters (or form/query). Provide the `owner`, `repo`, `title`, and `body`.

   Example using query parameters:
   ```bash
   curl -X POST "http://127.0.0.1:8000/create-issue/?owner=parulhardaha&repo=my-repo&title=Test+Issue&body=This+is+the+body"
   ```

   Response: GitHub API JSON for the created issue on success. If creation fails, the API returns `{"error": "Issue not created"}`.

## Notes & suggestions

- main.py now imports the route modules so that running `uvicorn main:app` will register the endpoints defined in the other files.
- `fetch.py` requests now include `headers` so authenticated requests use your token (recommended to avoid strict rate limits).
- Consider improving `POST /create-issue/` to accept a JSON body (via a Pydantic model) and use a path like `/repos/{owner}/{repo}/issues` to better match GitHub patterns.
- Ensure your `.env` is not committed to version control.

## Troubleshooting

- If endpoints are not visible, confirm `main.py` imports the route modules and that you are running `uvicorn main:app` from the project root.
- If you receive 401/403 from GitHub, verify your `GITHUB_TOKEN` in `.env` and that it has the required scopes.



## Security (token handling)

- If you accidentally expose a token (for example, in a recording or a commit), revoke it immediately on GitHub and create a new one. Go to GitHub Settings -> Developer settings -> Personal access tokens and delete the compromised token.
- For local development store the token in the project `.env` (this project already reads `GITHUB_TOKEN` using python-dotenv). Do NOT commit `.env` — it is included in `.gitignore`.
- Set restrictive permissions on the `.env` file so only your user can read it:

```bash
chmod 600 .env
```

- For more secure storage, use your OS keychain (macOS Keychain) or CI secrets for automation instead of files. In GitHub Actions, add the token under repository Settings -> Secrets and reference it in workflows as `${{ secrets.YOUR_SECRET_NAME }}`.


