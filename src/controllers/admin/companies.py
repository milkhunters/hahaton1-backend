from typing import Optional

from fastapi import APIRouter
from models import schemas
from services import repository

from views import ErrorAPIResponse
from views.companies import CompanyResponse

router = APIRouter(prefix="/company", responses={"400": {"model": ErrorAPIResponse}})


@router.get("/get", response_model=list[CompanyResponse])
async def get(company_id: Optional[int] = None, query: Optional[str] = None):
    if company_id:
        return await repository.company.get(id=company_id)
    if query:
        return await repository.company.get(query=query)
    return await repository.company.get()


@router.post("/update", response_model=CompanyResponse)
async def update(company_id: int, data: schemas.CompanyUpdate):
    return await repository.company.update(company_id, **data.dict(exclude_unset=True))


@router.post("/delete")
async def delete(company_id: int):
    await repository.company.delete(company_id)
