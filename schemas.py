from enum import Enum
from pydantic import BaseModel, Field

class IssueType(str, Enum):
    billing = "billing"
    technical = "technical"
    account = "account"
    other = "other"

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class SupportTicket(BaseModel):
    issue_type: IssueType = Field(
        description='Category of the customer issue'
    )
    summary: str = Field(
        description='Short summary of the issue in 1 sentence'
    )
    priority: Priority = Field(
        description='Urgency level of the issue'
    )
    action_required: bool = Field(
        description='Whether immediate action is required'
    )
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description='Confidence score between 0 and 1'
    )
