from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response
from config import load_docs
from dependencies import JWTCookie
from exceptions.api import APIError
from models import schemas
from services import repository

from views import ErrorAPIResponse, LoginResponse, RegisterResponse

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
docs = load_docs("review.ini")