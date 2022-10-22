from tortoise import fields, models

from models.state import PublicStates
from models.state import VerificationState


class PartnerVerificationInfo(models.Model):
    """
    The PartnerVerificationInfo model

    """
    id = fields.IntField(pk=True)
    status = fields.IntEnumField(enum_type=VerificationState)
    content = fields.TextField(null=True)
    partner = fields.ForeignKeyField('models.Partner', related_name="verification_info")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "partner_verification_info"


class Partner(models.Model):
    """
    The Partner model

    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100, unique=True)
    logo = fields.CharField(max_length=255)
    company = fields.ForeignKeyField('models.Company', related_name="partners")
    priority = fields.IntField(null=True)
    public_state = fields.IntEnumField(enum_type=PublicStates)
    verification_info: fields.ReverseRelation['PartnerVerificationInfo']
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "partners"
