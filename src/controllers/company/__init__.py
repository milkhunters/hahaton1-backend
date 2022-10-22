from fastapi import APIRouter

from views import ErrorAPIResponse

from . import partner
from . import portfolio
from . import review

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
router.include_router(partner.router, prefix="/partner", tags=["partner"])
router.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
router.include_router(review.router, prefix="/review", tags=["review"])
