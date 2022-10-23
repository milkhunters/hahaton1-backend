from typing import Optional, List, Union

from tortoise.expressions import Q
from tortoise.fields import CharField, IntField

from models.tables import Product
from services import repository
from src.models import tables
from models.state import VerificationState, PublicStates, PriceStates


async def get(id: int = None, query: str = None, *args, **kwargs) -> Union[List[tables.Product], tables.Product, None]:
    if query:
        fields = [f for f in tables.Product._meta.fields_map.values() if isinstance(f, CharField)]
        if query.isdigit():
            fields += [f for f in tables.Product._meta.fields_map.values() if isinstance(f, IntField)]
        queries = [Q(**{f.model_field_name: query}) for f in fields]
        qs = Q()
        for query in queries:
            qs |= query
        return await tables.Product.filter(qs)
    if id:
        return await tables.Product.filter(id=id).first()
    return await tables.Product.filter(*args, **kwargs).limit(40)


async def create(**kwargs) -> tables.Product:
    return await tables.Product.create(**kwargs)


async def update(product_id: int, **kwargs) -> tables.Product:
    product = await tables.Product.update_from_dict(await get(id=product_id), **kwargs)
    await product.save()
    return product


async def delete(product_id: int):
    product = await tables.Product.get_or_none(id=product_id)
    await product.delete()


async def verify_product(product_id: int, state: VerificationState, content: str = None):
    product = await tables.Product.get_or_none(id=product_id)
    await tables.ProductVerificationInfo.create(
        status=state,
        content=content,
        product=product
    )
    if state.verified:
        product.public_state = PublicStates.public
    elif state.denied:
        product.public_state = PublicStates.denied
    await product.save()


async def verify_product_category(product_category_id: int, state: VerificationState):
    product_category = await tables.ProductCategory.get_or_none(id=product_category_id)
    await tables.ProductCategoryVerificationInfo.create(
        status=state,
        product=product_category
    )
    if state.verified:
        product_category.public_state = PublicStates.public
    elif state.denied:
        product_category.public_state = PublicStates.denied
    await product_category.save()


async def create_catalog(company_id: int, **kwargs) -> tables.ProductCatalog:
    company = await repository.company.get(id=company_id)
    catalog = await tables.ProductCatalog.create(**kwargs)
    company.catalog = catalog
    await company.save()
    return catalog


async def create_category(catalog_id: int, **kwargs) -> tables.ProductCategory:
    catalog = await tables.ProductCatalog.get_or_none(id=catalog_id)
    category = await tables.ProductCategory.create(**kwargs)
    catalog.categories.add(category)
    await catalog.save()
    return category
