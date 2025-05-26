from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from models import PullRequestPayload
from github_utils import get_diff, comment_on_pr
from claude import review_with_claude
import os
import json

app = FastAPI(
    title="LLM GitHub PR Reviewer",
    description="Automatically reviews GitHub pull requests with Claude 3.5 Sonnet",
    version="1.0.0"
)

PROMPT_INSTRUCTIONS = """
You are an expert software reviewer. Please review the given code diff in a pull request.
Give constructive, actionable comments on things like:
- Logic issues
- Suggestions for better implementation
- Check for the time and space complexity, and confirm if they are optimal.
Only comment on what's in the diff.

##
Important: Do not comment more than 20 words.

In case if you find no major issues, simply generate a good one word comment to make the author feel good, you can be creative here, and it should put a smile on the author's face.

If you feel thhe author can improve the code or space or time complexity, please provide a detailed comment with suggestions.

Here is your final checklist, make sure to follow it, and dont forgot to leave a positive comment as the author took time to write this code:
Did Author mentioned Time Complexity :
Did Author mentioned Space Complexity :
Did Author gave comments explaining his approach

"""

@app.post("/webhook")
async def handle_pr_webhook(request: Request, ow : PullRequestPayload):

  payload = await request.json()
  print("Received payload:", json.dumps(payload, indent=2))

  if payload.get("action") != "opened":
      return {"message": "Ignored event"}

  pr = payload["pull_request"]
  repo = payload["repository"]["full_name"]
  pr_number = pr["number"]

  diff = await get_diff(repo, pr_number)
  review_comments = await review_with_claude(diff, PROMPT_INSTRUCTIONS)

  await comment_on_pr(repo, pr_number, review_comments)
  return {"message": "Review posted"}
