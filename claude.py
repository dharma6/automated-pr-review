import httpx
import os

from typing import Optional

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

if not ANTHROPIC_API_KEY:
    raise EnvironmentError("ANTHROPIC_API_KEY environment variable is not set.")


async def review_with_claude(diff: str, prompt_instructions: str) -> Optional[str]:
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "claude-3-5-sonnet-latest",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": f"{prompt_instructions}\n\nHere is the pull request diff:\n```diff\n{diff}\n```"
            }
        ]
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.post(CLAUDE_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['content'][0]['text']
