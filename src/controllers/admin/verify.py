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

router = APIRouter(prefix="/verify", responses={"400": {"model": ErrorAPIResponse}})
docs = load_docs("verify.py")


@router.post(
    "/exhibitor",
    response_model=UserResponse,
    # summary=docs["exhibitor"]["summary"],
    # description=docs["exhibitor"]["description"]
)
async def verify_exhibitor(exhibitor_id: int, comment: str, is_accept: bool):
    user = await repository.user.get_user(id=exhibitor_id)
    if not user:
        raise APIError(904)
    if UserStates(user.state_id) == UserStates.active:
        raise APIError(923)
    if is_accept:
        await repository.user.update_user(exhibitor_id, state_id=UserStates.active.value)
    else:
        await repository.user.update_user(exhibitor_id, state_id=UserStates.not_confirmed.value)


@router.post(
    "/product",
    response_model=UserResponse,
    # summary=docs["acceptProduct"]["summary"],
    # description=docs["acceptProduct"]["description"]
)
async def verify_product(product_id: int, comment: Optional[str], state: VerificationState):
    product = await repository.product.get(id=product_id)
    if not product:
        raise APIError(922)
    elif product.public_state == PublicStates.public:
        raise APIError(923)
    else:
        await repository.product.verify_product(product_id, state, comment)
    # TODO: добавить функцию, которая посылает комментарий на почту


async def verify_product_category(category_id: int, state: VerificationState):
    product_category = await repository.product.get(id=category_id)
    if not product_category:
        raise APIError(926)
