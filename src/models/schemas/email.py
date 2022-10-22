from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, validator, ValidationError


class Email(BaseModel):
    id: int
    email: str
    is_confirmed: bool
    company: Any
    create_time: datetime
    update_time: Optional[datetime]
