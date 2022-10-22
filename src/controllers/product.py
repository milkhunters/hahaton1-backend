from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response

from views import ErrorAPIResponse, LoginResponse, RegisterResponse

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})