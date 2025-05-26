import pytest
import respx
from httpx import Response
from claude import review_with_claude

API_URL = "https://api.anthropic.com/v1/messages"


@pytest.mark.asyncio
@respx.mock
async def test_review_with_claude():
    mock_response = {
        "content": [{"text": "Looks clean!"}]
    }

    respx.post(API_URL).mock(
        return_value=Response(200, json=mock_response)
    )

    result = await review_with_claude("diff --git ...", "Review this")
    assert result == "Looks clean!"
