from fastapi import APIRouter
from controllers import auth
from controllers import user
from controllers import stats
from controllers import file
from controllers import admin
from controllers import product
from controllers import company

from config import load_config

config = load_config()

root_api_router = APIRouter(prefix="/api/v1" if config.debug else "",)

root_api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
root_api_router.include_router(user.router, prefix="/user", tags=["User"])
root_api_router.include_router(file.router, prefix="/file", tags=["File"])
root_api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
root_api_router.include_router(product.router, prefix="/product", tags=["Stats"])
root_api_router.include_router(company.router, prefix="/company", tags=["Company"])
root_api_router.include_router(stats.router, tags=["Stats"])
