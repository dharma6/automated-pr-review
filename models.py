from pydantic import BaseModel

class PullRequestPayload(BaseModel):
    action: str
    pull_request: dict
    repository: dict
