from fastapi import APIRouter, Depends

from dependencies import JWTCookie, MinRoleFilter
from models.role import Role
from models.role import MainRole as M
from models.role import AdditionalRole as A


from views import ErrorAPIResponse

from . import admin, companies, product
from . import verify

router = APIRouter(
    responses={"400": {"model": ErrorAPIResponse}},
    dependencies=[Depends(JWTCookie()), Depends(MinRoleFilter(Role(M.moderator, A.one)))]
)
router.include_router(admin.router)
router.include_router(verify.router)
router.include_router(companies.router)
router.include_router(product.router)
