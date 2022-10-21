from tortoise import fields, models

from models.state import PriceStates, PublicStates
from models.state import ProductType, PurchaseType, ImportSubstitutionShield


class Product(models.Model):
    """
    The Product model
    """

    id = fields.IntField(pk=True)
    type = fields.IntEnumField(enum_type=ProductType)
    manufacturer = fields.CharField(max_length=255)
    trademark = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)
    # TODO: add imageS
    cover = fields.CharField(max_length=255, null=True)
    video = fields.CharField(max_length=255, null=True)
    description = fields.TextField(null=True)
    price = fields.FloatField()
    category = fields.ForeignKeyField('models.ProductCategory', related_name="products")
    purchase_type = fields.IntEnumField(enum_type=PurchaseType)
    min_lot = fields.IntField(default=1)

    # Payment Type fk
    # Delivery Type fk
    import_substitution_shield=fields.IntEnumField(ImportSubstitutionShield)
    compliance = fields.CharField(max_length=255, null=True)
    analogs = fields.CharField(max_length=255, null=True)
    public_state = fields.IntEnumField(enum_type=PublicStates)
    catalog = fields.ForeignKeyField('models.ProductCatalog', related_name="products")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "products"


class ProductCategory(models.Model):
    """
    The ProductCategory model
    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    catalog = fields.ForeignKeyField('models.ProductCatalog', related_name="categories")
    products = fields.ReverseRelation['Product']
    public_state = fields.IntEnumField(enum_type=PublicStates)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "product_categories"


class ProductCatalog(models.Model):
    """
    The ProductCatalog model
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    categories = fields.ReverseRelation['ProductCategory']
    products = fields.ReverseRelation['Product']
    price_state = fields.IntEnumField(enum_type=PriceStates)
    arbitrarily_price_text = fields.CharField(max_length=255, null=True)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "product_catalog"
