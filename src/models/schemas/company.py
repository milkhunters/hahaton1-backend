from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, validator, ValidationError
from tortoise import fields

from models.state import PublicStates
from models.state import VerificationState

from utils import validators
from .email import Email
from .product import Product
from .product import ProductCatalog
from .partner import Partner
from .portfolio import PortfolioCase


class Company(BaseModel):
    title: str
    description: Optional[str]
    about: Optional[str]
    logo: Optional[str]
    cover: Optional[str]
    category: Optional['CompanyCategory']
    exhibitor: Optional[Any]
    company_url: Optional[str]
    products: Optional[list['Product']]
    emails: Optional[list['Email']]
    catalog: Optional['ProductCatalog']
    partners: Optional[list['Partner']]
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
    id: int
    title: str
    companies: Optional[list['Company']]
    create_time: datetime
    update_time: Optional[datetime]


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
    update_time: Optional[datetime]


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


Company.update_forward_refs()
CompanyCategory.update_forward_refs()
CompanyLocation.update_forward_refs()
CompanyReview.update_forward_refs()
CompanyReviewVerificationInfo.update_forward_refs()
