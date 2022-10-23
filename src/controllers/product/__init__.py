from fastapi import APIRouter

from views import ErrorAPIResponse

from . import product, catalog

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
router.include_router(product.router)
router.include_router(catalog.router)