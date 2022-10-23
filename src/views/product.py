from typing import Optional

from pydantic import BaseModel, validator

from models import schemas


class ProductResponse(schemas.Product):
    pass
