from fastapi import APIRouter

from models import schemas
from services import repository

router = APIRouter(prefix="/catalog")


@router.post("/create", response_model=schemas.ProductCatalog)
async def create_catalog(company_id: int, catalog: schemas.ProductCatalogCreate):
    return await repository.product.create_catalog(company_id, **catalog.dict(exclude_unset=True))
