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

router = APIRouter(prefix="/product", responses={"400": {"model": ErrorAPIResponse}})


@router.get(
    "/getProducts"
)
async def get_products():
    return await repository.product.get_products()


@router.get(
    "/getProduct"
)
async def get_product(product_id: int):
    return await repository.product.get_products(id=product_id)

@router.get(
    "/getProduct"
)
async def get_product(product_id: int):
    return await repository.product.get_products(id=product_id)