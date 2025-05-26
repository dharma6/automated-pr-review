from fastapi import FastAPI, Request
from models import PullRequestPayload
from github_utils import get_diff, comment_on_pr
from claude import review_with_claude
import json

app = FastAPI(
    title="LLM GitHub PR Reviewer",
    description="Automatically reviews GitHub pull requests with Claude 3.5 Sonnet",
    version="1.0.0"
)

PROMPT_INSTRUCTIONS = """
You are an expert software reviewer. Please review the given code diff in a pull request.
Give constructive, actionable comments on:
- Logic issues
- Suggestions for better implementation
- Time and space complexity

Only comment on what's in the diff.

If no major issues are found, leave a creative one-word compliment to make the author smile.



Checklist:
- Did Author mention Time Complexity?
- Did Author mention Space Complexity?
- Did Author explain the approach with comments?
"""


@app.post("/webhook")
async def handle_pr_webhook(request: Request, payload: PullRequestPayload):
    print("Received payload:", json.dumps(payload.dict(), indent=2))

    if payload.action != "opened":
        return {"message": "Ignored event"}

    repo = payload.repository["full_name"]
    pr_number = payload.pull_request["number"]

    diff = await get_diff(repo, pr_number)
    review_comments = await review_with_claude(diff, PROMPT_INSTRUCTIONS)

    await comment_on_pr(repo, pr_number, review_comments)
    return {"message": "Review posted"}
