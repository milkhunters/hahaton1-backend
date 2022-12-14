import logging

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response

from config import load_docs
from dependencies import JWTCookie
from exceptions.api import APIError
from services.auth import authenticate, logout, refresh_tokens
from views import ErrorAPIResponse, RegisterResponse, UserResponse
from models import schemas
from services import repository

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
docs = load_docs("auth.ini")


@router.post(
    "/signUp",
    response_model=RegisterResponse,
    summary=docs["signUp"]["summary"],
    description=docs["signUp"]["description"]
)
async def sign_up(
        user: schemas.UserSignUp,
        is_auth=Depends(JWTCookie(auto_error=False)),
):
    if len(user.inn) != 12:
        raise APIError(api_code=911)
    if is_auth:
        raise APIError(920)
    if await repository.user.get(username__iexact=user.username):
        raise APIError(903)
    if await repository.user.get(email__iexact=user.email):
        raise APIError(925)
    if await repository.company.get(inn__iexact=user.inn):
        raise APIError(924)
    company = await repository.company.create(title=user.company_name, inn=user.inn)
    await repository.user.create_user(
        **user.dict(exclude={"inn", "company_name"}),
        company=company
    )


@router.post(
    "/signIn",
    response_model=UserResponse,
    summary=docs["signIn"]["summary"],
    description=docs["signIn"]["description"]
)
async def sign_in(
        user: schemas.UserSignIn,
        response: Response,
        is_auth=Depends(JWTCookie(auto_error=False))
):
    if is_auth:
        raise APIError(920)
    return await authenticate(user.username, user.password, response)


@router.post(
    '/logout',
    dependencies=[Depends(JWTCookie())],
    summary=docs["logout"]["summary"],
    description=docs["logout"]["description"]
)
async def logout_controller(request: Request, response: Response):
    await logout(request, response)


@router.post(
    '/refresh_tokens',
    dependencies=[Depends(JWTCookie())],
    summary=docs["refresh_tokens"]["summary"],
    description=docs["refresh_tokens"]["description"]
)
async def refresh(request: Request, response: Response):
    await refresh_tokens(request, response)
