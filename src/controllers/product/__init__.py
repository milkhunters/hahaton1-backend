from fastapi import APIRouter, Depends

from dependencies import JWTCookie
from views import ErrorAPIResponse

from . import product, catalog

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}}, dependencies=[Depends(JWTCookie())])
router.include_router(product.router)
router.include_router(catalog.router)