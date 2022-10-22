from fastapi import APIRouter

from views import ErrorAPIResponse

from . import product

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
router.include_router(product.router)
