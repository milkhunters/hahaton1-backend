from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, validator, ValidationError
from tortoise import fields

from models.state import PublicStates
from models.state import VerificationState, CaseContentType
from utils import validators


class PortfolioVerificationInfo(BaseModel):
    id: int
    status: VerificationState
    content: Optional[str]
    portfolio: Optional['PortfolioCase']
    create_time: datetime
    update_time: Optional[datetime]


class PortfolioCase(BaseModel):
    id: int
    title: str
    description: str
    partner_url: str
    content_type: CaseContentType
    content: str
    public_state: PublicStates
    verification_info: Optional[list[PortfolioVerificationInfo]]
    company: Any
    import_substitution_shield: bool
    create_time: datetime
    update_time: Optional[datetime]


PortfolioVerificationInfo.update_forward_refs()
PortfolioCase.update_forward_refs()
