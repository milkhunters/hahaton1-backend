from enum import Enum, unique


@unique
class UserStates(int, Enum):
    not_confirmed = 0
    active = 1
    blocked = 2
    deleted = 3


@unique
class PriceStates(int, Enum):
    visible = 0
    invisible = 1
    arbitrarily = 2


@unique
class PublicStates(int, Enum):
    public = 0
    private = 1
    denied = 2


@unique
class ProductType(int, Enum):
    product = 0
    service = 1


@unique
class PurchaseType(int, Enum):
    wholesale = 0
    retail = 1
    all = 2


@unique
class DeliveryType(int, Enum):
    pickup = 0
    delivery = 1
    pickup_and_delivery = 2


@unique
class PaymentType(int, Enum):
    cash = 0
    cashless = 1


@unique
class CaseContentType(int, Enum):
    html = 0
    video = 1


@unique
class VerificationState(int, Enum):
    not_verified = 0
    verified = 1
    denied = 2
