from typing import Optional, List

from models.tables import Product
from src.models import tables
from models.state import VerificationState, PublicStates


async def get(*args, **kwargs) -> Optional[tables.Product]:
    return await tables.Product.filter(*args, **kwargs).first()


async def get_products(*args, **kwargs) -> Optional[List[tables.Product]]:
    return await tables.Product.filter(*args, **kwargs)


async def create(**kwargs) -> tables.Product:
    return await tables.Product.create(**kwargs)


async def update(product_id: int, **kwargs) -> tables.Product:
    product = await tables.Product.update_from_dict(await get(id=product_id), **kwargs)
    await product.save()
    return product


async def delete(product_id: int) -> dict[str, Product | None]:
    product = await tables.Product.get_or_none(id=product_id)
    await product.delete()
    return {"resp": product}


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
