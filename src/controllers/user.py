import logging
from typing import Optional, Union, List

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response

from models import schemas, tables
from config import load_docs
from dependencies import JWTCookie
from exceptions.api import APIError
from services.auth import logout
from views import ErrorAPIResponse
from views import UserResponse
from views import UserOutResponse

from src.services import repository

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
docs = load_docs("auth.ini")


@router.get("/current", dependencies=[Depends(JWTCookie())], response_model=UserResponse)
async def get_current_user(request: Request):
    user = await repository.user.get(id=request.user.id)
    if not user:
        raise APIError(api_code=404)
    return user


@router.get("/get", response_model=Union[list[UserResponse], UserResponse])
async def get_user(
        user_id: Optional[int] = None,
        query: Optional[str] = None):
    if user_id:
        user = await repository.user.get(id=user_id)
    elif query:
        user = await repository.user.get(query=query)
    else:
        user = await repository.user.get()
    if not user:
        raise APIError(api_code=919)
    return user


@router.post("/update", dependencies=[Depends(JWTCookie())], response_model=UserResponse)
async def update_user(data: schemas.UserUpdate, request: Request):
    user = await repository.user.update_user(request.user.id, **data.dict(exclude_unset=True))
    return user


@router.delete("/delete", dependencies=[Depends(JWTCookie())])
async def delete_user(request: Request, response: Response):
    await logout(request, response)
    await repository.user.delete(request.user.id)
