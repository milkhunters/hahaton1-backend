from fastapi import APIRouter

from models import schemas
from services import repository

router = APIRouter(prefix="/catalog")


@router.post("/create", response_model=schemas.ProductCatalog)
async def create_catalog(company_id: int, catalog: schemas.ProductCatalogCreate):
    return await repository.product.create_catalog(company_id, **catalog.dict(exclude_unset=True))


@router.post("/createCategory", response_model=schemas.ProductCategory)
async def create_category(catalog_id: int, category: schemas.ProductCategory):
    return await repository.product.create_category(catalog_id, **category.dict(exclude_unset=True))


@router.post("/updateCategory", response_model=schemas.ProductCategory)
async def update_category(category_id: int, category: schemas.ProductCategory):
    return await repository.product.update_category(category_id, **category.dict(exclude_unset=True))


@router.post("/deleteCategory", response_model=schemas.ProductCategory)
async def delete_category(category_id: int):
    return await repository.product.delete_category(category_id)

