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

# === CREATE PULL REQUEST ===
pr = repo.create_pull(
    title=PR_TITLE,
    body=PR_BODY,
    head=SOURCE_BRANCH,
    base=TARGET_BRANCH
)
print(f"Created PR: {pr.html_url}")

# === CLOSE PULL REQUEST ===
# Uncomment this if you want to close it immediately
# pr.edit(state="closed")
# print(f"Closed PR #{pr.number}")
