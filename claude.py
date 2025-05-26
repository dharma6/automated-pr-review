import httpx
import os

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

async def review_with_claude(diff: str, prompt_instructions: str):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }

    messages = [
        {
            "role": "user",
            "content": f"{prompt_instructions}\n\nHere is the pull request diff:\n```diff\n{diff}\n```"
        }
    ]

    payload = {
        "model": "claude-3-5-sonnet-latest",
        "max_tokens": 1024,
        "messages": messages
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        return response.json()['content'][0]['text']
