from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, ValidationError

from models.state import VerificationState, PublicStates


class PartnerVerificationInfo(BaseModel):
    id: int
    status: VerificationState
    content: str
    partner: Optional['Partner']
    create_time: datetime
    update_time: Optional[datetime]


class Partner(BaseModel):
    id: int
    title: str
    logo: str
    company: Optional['Company']
    priority: Optional[int]
    public_state: PublicStates
    verification_info: Optional['PartnerVerificationInfo']
    create_time: datetime
    update_time: Optional[datetime]