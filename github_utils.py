import httpx
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is not set")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

async def get_diff(repo: str, pr_number: int) -> str:
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    diff_headers = headers.copy()
    diff_headers["Accept"] = "application/vnd.github.v3.diff"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=diff_headers)
        response.raise_for_status()
        return response.text

async def comment_on_pr(repo_full_name, pr_number, body):
    url = f"https://api.github.com/repos/{repo_full_name}/issues/{pr_number}/comments"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json={"body": body})
        response.raise_for_status()
        print(f"Commented on PR #{pr_number}")
