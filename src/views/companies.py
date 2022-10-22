from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, validator


class CompanyResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    about: Optional[str]
    logo: Optional[str]
    cover: Optional[str]
    exhibitor: Optional[Any]
    company_url: Optional[str]
    phone_number: Optional[str]
    inn: str
    legal_address: Optional[str]
    manufacture_address: Optional[str]
    import_substitution_shield: Optional[bool]
    create_time: datetime
    update_time: Optional[datetime]
