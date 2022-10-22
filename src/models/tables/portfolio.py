from tortoise import fields, models

from models.state import CaseContentType, PublicStates, VerificationState


class PortfolioVerificationInfo(models.Model):
    """
    The ProductVerificationInfo model

    """
    id = fields.IntField(pk=True)
    status = fields.IntEnumField(enum_type=VerificationState)
    content = fields.TextField(null=True)
    product = fields.ForeignKeyField('models.PortfolioCase', related_name="verification_info")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "portfolio_verification_info"


class PortfolioCase(models.Model):
    """
    The Portfolio Case model

    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100, unique=True)
    description = fields.TextField(max_length=1000, min_length=1)
    partner_url = fields.CharField(max_length=255)
    content_type = fields.IntEnumField(enum_type=CaseContentType)
    content = fields.TextField()
    public_state = fields.IntEnumField(enum_type=PublicStates)
    verification_info: fields.ReverseRelation["PortfolioVerificationInfo"]
    company = fields.ForeignKeyField('models.Company', related_name="cases")
    import_substitution_shield = fields.BooleanField(default=False)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "portfolio_cases"
