from fastapi import APIRouter, Depends

from dependencies import JWTCookie
from views import ErrorAPIResponse

from . import product

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}}, dependencies=[Depends(JWTCookie())])
router.include_router(product.router)
