import pytest
import respx
import json
import asyncio
from httpx import Response
from github_utils import get_diff, comment_on_pr


class TestGitHubAPIIntegration:
    """Integration tests for GitHub API interactions."""

    @pytest.mark.asyncio
    @respx.mock
    async def test_get_diff_success(self):
        """Test successful diff retrieval from GitHub API."""
        repo = "owner/repo"
        pr_number = 42
        expected_diff = """diff --git a/file.py b/file.py
index abc123..def456 100644
--- a/file.py
+++ b/file.py
@@ -1,3 +1,4 @@
 def hello():
+    # Added comment
     print("Hello")
"""

        respx.get(f"https://api.github.com/repos/{repo}/pulls/{pr_number}").mock(
            return_value=Response(
                200,
                text=expected_diff,
                headers={"Content-Type": "application/vnd.github.v3.diff"}
            )
        )

        result = await get_diff(repo, pr_number)

        assert result == expected_diff

        # Verify request was made with correct headers
        request = respx.calls[0].request
        assert request.headers["Accept"] == "application/vnd.github.v3.diff"
        assert "token" in request.headers["Authorization"]

    @pytest.mark.asyncio
    @respx.mock
    async def test_comment_on_pr_success(self):
        """Test successful comment posting to PR."""
        repo = "owner/repo"
        pr_number = 42
        comment_body = "This looks great! Well done on the implementation."

        expected_response = {
            "id": 123456,
            "body": comment_body,
            "user": {"login": "automated-reviewer"},
            "created_at": "2023-01-01T12:00:00Z"
        }

        respx.post(f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments").mock(
            return_value=Response(201, json=expected_response)
        )

        await comment_on_pr(repo, pr_number, comment_body)

        # Verify request was made correctly
        request = respx.calls[0].request
        assert request.headers["Authorization"].startswith("token")
        assert request.headers["Accept"] == "application/vnd.github.v3+json"

        request_body = json.loads(request.content)
        assert request_body["body"] == comment_body

    @pytest.mark.asyncio
    @respx.mock
    async def test_github_api_error_handling(self):
        """Test handling of various GitHub API errors."""
        repo = "owner/repo"
        pr_number = 999

        # Test 404 error
        respx.get(f"https://api.github.com/repos/{repo}/pulls/{pr_number}").mock(
            return_value=Response(404, json={"message": "Not Found"})
        )

        with pytest.raises(Exception):
            await get_diff(repo, pr_number)

    @pytest.mark.asyncio
    @respx.mock
    async def test_comment_with_markdown(self):
        """Test commenting with markdown-formatted content."""
        repo = "owner/repo"
        pr_number = 42

        markdown_comment = """## Code Review Summary
**Issues Found:**
- ❌ Missing error handling
- ⚠️ Consider using async/await

**Overall:** Good work! 🎉"""

        respx.post(f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments").mock(
            return_value=Response(201, json={"id": 789, "body": markdown_comment})
        )

        await comment_on_pr(repo, pr_number, markdown_comment)

        request = respx.calls[0].request
        request_body = json.loads(request.content)
        assert "## Code Review Summary" in request_body["body"]
        assert "🎉" in request_body["body"]
