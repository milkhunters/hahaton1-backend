from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, ValidationError
from tortoise import fields

from utils import validators


class Company(BaseModel):
    pass
