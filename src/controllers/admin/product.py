from typing import Optional, Union

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response

import views
from config import load_docs
from dependencies import JWTCookie
from exceptions.api import APIError
from models import schemas
from models.state import VerificationState, UserStates, PublicStates
from services import repository

from views import ErrorAPIResponse, UserOutResponse, LoginResponse, RegisterResponse, UserResponse

router = APIRouter(prefix="/product", responses={"400": {"model": ErrorAPIResponse}})


