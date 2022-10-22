from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, ValidationError
from tortoise import fields

from models.schemas.company import Company
from models.state import VerificationState, ProductType, PurchaseType, PaymentType, DeliveryType, PublicStates, \
    PriceStates
from utils import validators


class ProductImages(BaseModel):
    id: int
    image: str
    product: 'Product'


class ProductVerificationInfo(BaseModel):
    id: int
    status: VerificationState
    content: Optional[str]
    product: 'Product'
    create_time: datetime
    update_time: Optional[datetime]


class Product(BaseModel):
    """
    The Product model
    """

    id: int
    type: ProductType
    manufacturer: str
    trademark: str
    title: str
    images: Optional[list['ProductImages']]
    cover: Optional[str]
    video: Optional[str]
    description: Optional[str]
    price: float
    company: Optional['Company']
    category: Optional['ProductCategory']
    purchase_type: PurchaseType
    min_lot: Optional[int]
    payment_type: PaymentType
    delivery_type: DeliveryType
    import_substitution_shield: bool
    compliance: Optional[str]
    analogs: Optional[str]
    public_state: PublicStates
    catalog: Optional['ProductCatalog']
    verification_info: Optional[list[ProductVerificationInfo]]
    create_time: datetime
    update_time: Optional[datetime]


class ProductCategoryVerificationInfo(BaseModel):
    """
    The ProductCategoryVerificationInfo model

    """
    id: int
    status: VerificationState
    content: Optional[str]
    product: Optional['ProductCategory']
    create_time: datetime
    update_time: Optional[datetime]


class ProductCategory(BaseModel):
    """
    The ProductCategory model
    """
    id: int
    title: str
    catalog: Optional['ProductCatalog']
    products: Optional[list['Product']]
    verification_info: Optional[list['ProductCategoryVerificationInfo']]
    public_state: PublicStates
    create_time: datetime
    update_time: Optional[datetime]


class ProductCatalog(BaseModel):
    """
    The ProductCatalog model
    """

    id: int
    title: str
    categories: Optional[list['ProductCategory']]
    products: Optional[list['Product']]
    companies: Optional[list['Company']]
    price_state: PriceStates
    arbitrarily_price_text: Optional[str]
    create_time: datetime
    update_time: Optional[datetime]
