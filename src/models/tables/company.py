from tortoise import fields, models

from models.state import PublicStates, VerificationState


class Company(models.Model):
    """
    The Company model
    """
    title = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    about = fields.TextField(null=True)
    logo = fields.CharField(max_length=255, null=True)
    cover = fields.CharField(max_length=255, null=True)
    category = fields.ForeignKeyField('models.CompanyCategories', related_name="companies", null=True)
    exhibitor: fields.ReverseRelation['User']
    company_url = fields.CharField(255, null=True)
    products: fields.ReverseRelation["product"]
    emails: fields.ReverseRelation['Email']
    catalog = fields.ForeignKeyField('models.ProductCatalog', related_name="companies", null=True)
    partners = fields.ReverseRelation['Partner']
    locations: fields.ReverseRelation['CompanyLocation']
    reviews: fields.ReverseRelation['CompanyReview']
    cases: fields.ReverseRelation['PortfolioCase']
    phone_number = fields.CharField(max_length=20, null=True)  # тк международные номера лайк
    inn = fields.CharField(max_length=12, unique=True)
    legal_address = fields.TextField(null=True)
    manufacture_address = fields.TextField(null=True)
    import_substitution_shield = fields.BooleanField(default=False)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "companies"


class CompanyCategories(models.Model):
    """
    The Categories model
    """

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    companies = fields.ReverseRelation['Company']
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "company_categories"


class CompanyLocation(models.Model):
    """
    The Company Location model
    """
    id = fields.IntField(pk=True)
    company = fields.ForeignKeyField('models.Company', related_name="locations")
    address = fields.CharField(max_length=512)
    coordinates = fields.CharField(max_length=512)
    title = fields.CharField(max_length=255)
    location_type = fields.CharField(max_length=255)
    partner_url = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "company_locations"


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
