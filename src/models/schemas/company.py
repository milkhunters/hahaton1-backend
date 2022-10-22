from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, ValidationError
from tortoise import fields

from models import PublicStates
from models.state import VerificationState
from utils import validators


class Company(BaseModel):
    title: str
    description: Optional[str]
    about: Optional[str]
    logo: Optional[str]
    cover: Optional[str]
    category: Optional['CompanyCategory']
    exhibitor: 'User'  # исключать, когда вложение
    company_url: Optional[str]
    products: Optional[list['Product']]
    emails: Optional[list['Email']]
    catalog: Optional['ProductCatalog']
    partners = Optional[list['Partner']]
    locations: Optional[list['CompanyLocation']]
    reviews: Optional[list['CompanyReview']]
    cases: Optional[list['PortfolioCase']]
    phone_number: Optional[str]
    inn: str
    legal_address: Optional[str]
    manufacture_address: Optional[str]
    import_substitution_shield: Optional[bool]
    create_time: datetime
    update_time: Optional[datetime]


class CompanyCategory(BaseModel):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    companies = fields.ReverseRelation['Company']
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

class CompanyLocation(BaseModel):
    id: int
    company: Optional['Company']
    address: str
    coordinates: str
    title: str
    location_type: str
    partner_url: str
    is_active: bool
    create_time: datetime
    update_time: datetime


class CompanyReviewVerificationInfo(BaseModel):
    id: int
    status: VerificationState
    content: Optional[str]
    review: Optional['CompanyReview']
    create_time: datetime
    update_time: Optional[datetime]


class CompanyReview(BaseModel):
    id: int
    company: Optional['Company']
    creator: Optional[str]
    content: str
    rating: float
    img: Optional[str]
    public_state: PublicStates
    verification_info: Optional[list['CompanyReviewVerificationInfo']]
    create_time: datetime
    update_time: Optional[datetime]
