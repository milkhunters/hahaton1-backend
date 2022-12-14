from typing import List, Optional, Dict, Union
from tortoise.expressions import Q
from tortoise.fields import CharField, IntField

from models.tables import Company
from src.models import tables
from src.models import Role, A, M
from src.models import UserStates
from src.utils import get_hashed_password


async def get(
        query: str = None,
        *args, **kwargs
) -> Union[List[tables.Company], tables.Company, None]:
    if query:
        fields = [f for f in tables.Company._meta.fields_map.values() if isinstance(f, CharField)]
        if query.isdigit():
            fields += [f for f in tables.Company._meta.fields_map.values() if isinstance(f, IntField)]
        queries = [Q(**{f.model_field_name: query}) for f in fields]
        qs = Q()
        for query in queries:
            qs |= query

        companies = await tables.Company.filter(qs).limit(40)
        if companies:
            await tables.Company.fetch_for_list(companies, "exhibitor")
        return companies


    if set(kwargs) & set([f.model_field_name for f in tables.Company._meta.fields_map.values() if f.unique]):
        company = await tables.Company.get_or_none(*args, **kwargs)
        if company:
            await tables.Company.fetch_related(company, "exhibitor")
        return company

    companies = await tables.Company.filter(*args, **kwargs).limit(40)
    if companies:
        await tables.Company.fetch_for_list(companies, "exhibitor")
    return companies



async def create(**kwargs) -> tables.Company:
    return await tables.Company.create(**kwargs)


async def update(company_id: int, **kwargs) -> tables.Company:
    company = await tables.Company.update_from_dict(await get(id=company_id), kwargs)
    await company.save()
    return company


async def delete(company_id: int):
    company = await tables.Company.get_or_none(id=company_id)
    await company.delete()

