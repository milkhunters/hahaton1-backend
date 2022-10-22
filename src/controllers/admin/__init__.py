from fastapi import APIRouter

from views import ErrorAPIResponse

from . import admin
from . import verify

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
router.include_router(admin.router)
router.include_router(verify.router)
