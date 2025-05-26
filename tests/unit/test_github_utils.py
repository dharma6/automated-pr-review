import pytest
import respx
from httpx import Response
from github_utils import get_diff, comment_on_pr

REPO = "user/repo"
PR_NUMBER = 1
BASE_URL = "https://api.github.com"


@pytest.mark.asyncio
@respx.mock
async def test_get_diff():
    expected_diff = "diff --git ..."
    respx.get(f"{BASE_URL}/repos/{REPO}/pulls/{PR_NUMBER}").mock(
        return_value=Response(200, text=expected_diff, headers={"Content-Type": "application/vnd.github.v3.diff"})
    )
    result = await get_diff(REPO, PR_NUMBER)
    assert result == expected_diff


@pytest.mark.asyncio
@respx.mock
async def test_comment_on_pr():
    respx.post(f"{BASE_URL}/repos/{REPO}/issues/{PR_NUMBER}/comments").mock(
        return_value=Response(201)
    )
    await comment_on_pr(REPO, PR_NUMBER, "Looks great!")
