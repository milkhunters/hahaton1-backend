from tortoise import fields, models

from models.state import PriceStates, PublicStates, DeliveryType, PaymentType, VerificationState
from models.state import ProductType, PurchaseType


class ProductImages(models.Model):
    """
    The ProductImages model

    """
    id = fields.IntField(pk=True)
    image = fields.CharField(max_length=255)
    product = fields.ForeignKeyField('models.Product', related_name="images")

    class Meta:
        table = "product_images"


class ProductVerificationInfo(models.Model):
    """
    The ProductVerificationInfo model

    """
    id = fields.IntField(pk=True)
    status = fields.IntEnumField(enum_type=VerificationState)
    content = fields.TextField(null=True)
    product = fields.ForeignKeyField('models.Product', related_name="verification_info")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "product_verification_info"


class Product(models.Model):
    """
    The Product model
    """

    id = fields.IntField(pk=True)
    type = fields.IntEnumField(enum_type=ProductType)
    manufacturer = fields.CharField(max_length=255)
    trademark = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)
    images: fields.ReverseRelation['ProductImages']
    cover = fields.CharField(max_length=255, null=True)
    video = fields.CharField(max_length=255, null=True)
    description = fields.TextField(null=True)
    price = fields.FloatField()
    company = fields.ForeignKeyField('models.Company', related_name="products")
    category = fields.ForeignKeyField('models.ProductCategory', related_name="products")
    purchase_type = fields.IntEnumField(enum_type=PurchaseType)
    min_lot = fields.IntField(default=1)
    payment_type = fields.IntEnumField(enum_type=PaymentType)
    delivery_type = fields.IntEnumField(enum_type=DeliveryType)
    import_substitution_shield = fields.BooleanField(default=False)
    compliance = fields.CharField(max_length=255, null=True)
    analogs = fields.CharField(max_length=255, null=True)
    public_state = fields.IntEnumField(enum_type=PublicStates)
    catalog = fields.ForeignKeyField('models.ProductCatalog', related_name="products")
    verification_info: fields.ReverseRelation['ProductVerificationInfo']
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "products"


class ProductCategoryVerificationInfo(models.Model):
    """
    The ProductCategoryVerificationInfo model

    """
    id = fields.IntField(pk=True)
    status = fields.IntEnumField(enum_type=VerificationState)
    content = fields.TextField(null=True)
    product = fields.ForeignKeyField('models.ProductCategory', related_name="verification_info")
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "product_category_verification_info"


class ProductCategory(models.Model):
    """
    The ProductCategory model
    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    catalog = fields.ForeignKeyField('models.ProductCatalog', related_name="categories")
    products = fields.ReverseRelation['Product']
    verification_info: fields.ReverseRelation['ProductCategoryVerificationInfo']
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
    title = fields.CharField(max_length=255)
    categories = fields.ReverseRelation['ProductCategory']
    products = fields.ReverseRelation['Product']
    companies = fields.ReverseRelation['Company']
    price_state = fields.IntEnumField(enum_type=PriceStates)
    arbitrarily_price_text = fields.CharField(max_length=255, null=True)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "product_catalog"
