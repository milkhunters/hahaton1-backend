from tortoise import fields, models


class Email(models.Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=100, unique=True)
    # is_confirmed = fields.BooleanField(default=False)
    owner = fields.ForeignKeyField('models.User', related_name="emails")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)
