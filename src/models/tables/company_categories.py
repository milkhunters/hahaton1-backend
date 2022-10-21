from tortoise import fields, models


class Categories(models.Model):
    """
    The Categories model
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    subcategories = fields.ReverseRelation["SubCategories"]
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "categories"


class SubCategories(models.Model):
    """
    The SubCategories model
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    parent = fields.ForeignKeyField('models.Categories', related_name="subcategories")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "sub_categories"
