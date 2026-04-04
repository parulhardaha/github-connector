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

1. Clone the repository:

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

4. Create a `.env` file in the project root with GitHub token:

   ```text
   GITHUB_TOKEN=ghp_...your_token_here...
   ```

## How to run

Run the FastAPI app with uvicorn:

```bash
uvicorn main:app --reload
```

## API endpoints

Base URL: `http://127.0.0.1:8000`

1. GET `/` — Home


2. GET `/repos/{username}` — List a user's repositories

   Path parameters:
   - `username` — GitHub username to fetch repos for.

3. GET `/issues/{owner}/{repo}` — List issues in a repository

   Path parameters:
   - `owner` — repository owner (user or org)
   - `repo` — repository name

4. POST `/create-issue/` — Create a new issue

   Current implementation expects these parameters as query parameters (or form/query). Provide the `owner`, `repo`, `title`, and `body`.

