from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, ValidationError
from tortoise import fields

from models import PublicStates
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
    company = fields.ForeignKeyField('models.Company', related_name="cases")
    import_substitution_shield = fields.BooleanField(default=False)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)
