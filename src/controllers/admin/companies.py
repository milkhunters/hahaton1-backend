from typing import Optional

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response
from config import load_docs
from dependencies import JWTCookie
from exceptions.api import APIError
from models import schemas
from models.state import VerificationState, UserStates, PublicStates
from services import repository

from views import ErrorAPIResponse, UserOutResponse, LoginResponse, RegisterResponse, UserResponse

router = APIRouter(prefix="/company", responses={"400": {"model": ErrorAPIResponse}})


@router.get(
    "/getCompanies"
)
async def get_companies():
    return await repository.company.get_companies()


@router.get(
    "/getCompany"
)
async def get_company(company_id: int):
    return await repository.company.get(id=company_id)


# Удалить компанию по id, а вместе с ней пользователя, продукты, отзывы, месторасположение, категории

@router.get(
    "/deleteCompany"
)
async def delete_company(company_id: int):
    return await repository.company.delete(company_id=company_id)


@router.get(
    "/updateCompany"
)
async def update_company(company_id: int, company ):
    return {"resp":await repository.company.update(company_id, )}

