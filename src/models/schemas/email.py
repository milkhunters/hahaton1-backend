from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, ValidationError


class Email(BaseModel):
    id: int
    email: str
    is_confirmed: bool
    company: Optional['Company']
    create_time = datetime
    update_time = Optional[datetime]

