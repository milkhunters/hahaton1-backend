from tortoise import fields, models
from ..role import Role, MainRole as M, AdditionalRole as A
from ..state import UserStates as S


class Exhibitor(models.Model):
    """
    The Exhibitor model
    """

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    description = fields.TextField()
    logo = fields.CharField(max_length=255)
    cover = fields.CharField(max_length=255)
    # категория
    company_url = fields.CharField(255)
    username = fields.CharField(max_length=30, unique=True)
    hashed_password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=100, unique=True) # pk таблица
    notification_email = fields.CharField(max_length=100, unique=True)
    phone_number = fields.CharField(max_length=20)  # тк международные номера лайк
    full_name = fields.CharField(max_length=64)
    inn = fields.IntField()
    legal_address = fields.TextField()
    manufacture_address = fields.TextField()
    role_id = fields.IntField(default=Role(M.user, A.one))
    state_id = fields.IntField(default=S.not_confirmed.value)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class PydanticMeta:
        exclude = ["hashed_password"]


class ExhibitorDeleted(models.Model):
    id = fields.IntField(pk=True)
    delete_time = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "exhibitor_deleted"
