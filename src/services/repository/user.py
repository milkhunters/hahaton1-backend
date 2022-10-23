from typing import List, Optional, Union
from tortoise.expressions import Q
from tortoise.fields import CharField, IntField

from src.models import tables
from src.models import Role, A, M
from src.models import UserStates
from src.utils import get_hashed_password


async def get(
        query: str = None,
        *args, **kwargs
) -> Union[List[tables.User], tables.User, None]:
    if query:
        fields = [f for f in tables.User._meta.fields_map.values() if isinstance(f, CharField)]
        if query.isdigit():
            fields += [f for f in tables.User._meta.fields_map.values() if isinstance(f, IntField)]
        queries = [Q(**{f.model_field_name: query}) for f in fields]
        qs = Q()
        for query in queries:
            qs |= query

        users = await tables.User.filter(qs).limit(40)
        await tables.User.fetch_for_list(users, "company")
        return users

    if set(kwargs) & set([f.model_field_name for f in tables.User._meta.fields_map.values() if f.unique]):
        user = await tables.User.filter(**kwargs).first()
        await user.fetch_related("company")
        return user
    users = await tables.User.filter(*args, **kwargs).limit(40)
    await tables.User.fetch_for_list(users, "company")
    return users


async def get_users(*args, **kwargs) -> Optional[List[tables.User]]:
    return await tables.User.filter(*args, **kwargs)


async def create_user(**kwargs) -> tables.User:
    return await tables.User.create(
        role_id=Role(M.user, A.one).value(),
        state_id=UserStates.not_confirmed.value,
        hashed_password=get_hashed_password(kwargs.pop("password")),
        **kwargs
    )


async def update_user(user_id: int, **kwargs) -> tables.User:
    user = await tables.User.update_from_dict(await get(id=user_id), kwargs)
    await user.save()
    return user


async def delete(user_id: int) -> None:
    await update_user(user_id, state_id=UserStates.deleted.value)
    await tables.UserDeleted.create(id=user_id)
