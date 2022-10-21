from enum import Enum, unique


@unique
class UserStates(Enum):
    not_confirmed = 0
    active = 1
    blocked = 2
    deleted = 3


@unique
class PriceStates(Enum):
    visible = 0
    invisible = 1
    arbitrarily = 2


@unique
class PublicStates(Enum):
    public = 0
    private = 1
    denied = 2


@unique
class ProductType(Enum):
    product = 0
    service = 1


@unique
class PurchaseType(Enum):
    wholesale = 0
    retail = 1


@unique
class ImportSubstitutionShield(Enum):
    no = 0
    yes = 1
