from pydantic import BaseModel
from typing import Dict


class PullRequestPayload(BaseModel):
    action: str
    pull_request: Dict
    repository: Dict
