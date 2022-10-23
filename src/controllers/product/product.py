from typing import Optional, Union

from fastapi import APIRouter

from models import schemas
from models.state import VerificationState, UserStates, PublicStates
from services import repository

import views

router = APIRouter()


@router.get("/get", response_model=Union[list[views.ProductResponse], views.ProductResponse])
async def get(product_id: Optional[int] = None, query: Optional[str] = None):
    await repository.product.get(query=query, id=product_id)


@router.post("/update", response_model=views.ProductResponse)
async def update(product_id: int, data: schemas.ProductUpdate):
    await repository.product.update(product_id, **data.dict(exclude_unset=True))


@router.delete("/delete")
async def delete(product_id: int):
    await repository.product.delete(product_id)
