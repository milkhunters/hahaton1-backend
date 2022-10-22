from tortoise import fields, models

from models.state import PublicStates
from models.state import VerificationState


class CompanyReviewVerificationInfo(models.Model):
    """
    The CompanyReviewVerificationInfo model

    """
    id = fields.IntField(pk=True)
    status = fields.IntEnumField(enum_type=VerificationState)
    content = fields.TextField(null=True)
    product = fields.ForeignKeyField('models.CompanyReview', related_name="verification_info")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "company_review_verification_info"


class CompanyReview(models.Model):
    """
    The CompanyReview model

    """
    id = fields.IntField(pk=True)
    company = fields.ForeignKeyField('models.Company', related_name="reviews")
    creator = fields.CharField(max_length=100)
    content = fields.TextField(max_length=1000, min_length=1)
    rating = fields.FloatField()
    img = fields.CharField(max_length=255, null=True)
    public_state = fields.IntEnumField(enum_type=PublicStates)
    verification_info: fields.ReverseRelation['CompanyReviewVerificationInfo']
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "company_reviews"
