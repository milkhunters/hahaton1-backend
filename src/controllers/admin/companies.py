from typing import Optional

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response
from config import load_docs
from dependencies import JWTCookie
from exceptions.api import APIError
from models import schemas
from services import repository

from views import ErrorAPIResponse, UserOutResponse, LoginResponse, RegisterResponse
from views.companies import CompanyResponse

router = APIRouter(prefix="/company", responses={"400": {"model": ErrorAPIResponse}})


@router.get("/get", response_model=list[CompanyResponse])
async def get_companies(query: Optional[str] = None):
    return await repository.company.get_companies(query)
