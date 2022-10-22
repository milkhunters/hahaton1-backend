from tortoise import fields, models
from ..role import Role, MainRole as M, AdditionalRole as A
from ..state import UserStates as S


class User(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=64)
    username = fields.CharField(max_length=30, unique=True)
    hashed_password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=100, unique=True)
    company = fields.OneToOneField('models.Company', related_name="exhibitor", null=True)
    role_id = fields.IntField(default=Role(M.user, A.one))
    state_id = fields.IntField(default=S.not_confirmed.value)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class PydanticMeta:
        exclude = ["hashed_password"]


class UserDeleted(models.Model):
    id = fields.IntField(pk=True)
    delete_time = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_deleted"
