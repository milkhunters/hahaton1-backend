from tortoise import fields, models


class CompanyCategories(models.Model):
    """
    The Categories model
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    companies = fields.ReverseRelation['User']
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "company_categories"
