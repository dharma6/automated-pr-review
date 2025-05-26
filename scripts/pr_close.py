from  github import Github

import os
# === CONFIGURATION ===
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "dharma6/agrow_help"  # e.g., octocat/Hello-World
SOURCE_BRANCH = "test_review"
TARGET_BRANCH = "main"
PR_TITLE = "Add new feature"
PR_BODY = "This pull request adds a new feature."

# === AUTHENTICATION ===
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
open_prs = repo.get_pulls(state='open', sort='created')

if open_prs.totalCount == 0:
    print("No open pull requests found.")
else:
    for pr in open_prs:
        print(f"Closing PR #{pr.number}: {pr.title}")
        pr.edit(state="closed")

    print(f"✅ Closed {open_prs.totalCount} open pull request(s).")
