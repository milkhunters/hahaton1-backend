from typing import List, Optional
from tortoise.expressions import Q

from src.models import tables
from src.models import Role, A, M
from src.models import UserStates
from src.utils import get_hashed_password


async def get(*args, **kwargs) -> Optional[tables.Company]:
    return await tables.Company.filter(*args, **kwargs).first()


async def get_companies(*args, **kwargs) -> Optional[List[tables.Company]]:
    return await tables.Company.filter(*args, **kwargs)


async def create(**kwargs) -> tables.Company:
    return await tables.Company.create(**kwargs)


async def update(company_id: int, **kwargs) -> tables.Company:
    company = await tables.Company.update_from_dict(await get(id=company_id), kwargs)
    await company.save()
    return company


async def delete(company_id: int) -> None:
    ...
