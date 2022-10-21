from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, ValidationError
from tortoise import fields

from utils import validators


class User(BaseModel):
    """
    Базовая схема пользователя
    """
    id: int
    title:  Optional[str]
    description:  Optional[str]
    logo:  Optional[str]
    cover:  Optional[str]
    company_url:  Optional[str]
    category_id: int
    username:  Optional[str]
    notification_email:  Optional[str]
    phone_number: str
    email: str
    full_name: str
    inn:  Optional[str]
    legal_address:  Optional[str]
    manufacture_address:  Optional[str]
    role_id: int
    state_id: int
    create_time: datetime
    update_time: datetime

    @validator("*", pre=True, each_item=False)
    def _tortoise_convert(cls, value):
        """
        Необходимо для преобразования
        некоторых вызываемых полей модели
        и для Reverse и ManyToMany связей

        :param value:
        :return:
        """
        # Вызываемые поля
        if callable(value):
            return value()
        # Конвертирование ManyToManyRelation в список
        if isinstance(value, (fields.ManyToManyRelation, fields.ReverseRelation)):
            return list(value)
        return value

    class Config:
        orm_mode = True


class UserSignUp(BaseModel):
    username: str
    password: str
    email: list[str]
    title: str
    inn: str
    notification_email: str
    phone_number: str
    description: str
    legal_address: int


    @validator('username')
    def username_len(cls, value):
        if not validators.is_valid_username(value):
            raise ValidationError
        return value

    @validator('email')
    def email_must_be_valid(cls, value):
        if not validators.is_valid_email(value):
            raise ValidationError
        return value

    @validator('password')
    def password_must_be_valid(cls, value):
        if not validators.is_valid_password(value):
            raise ValidationError
        return value


class UserSignIn(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_len(cls, value):
        if not validators.is_valid_username(value):
            raise ValidationError
        return value

    @validator('password')
    def password_must_be_valid(cls, value):
        if not validators.is_valid_password(value):
            raise ValidationError
        return value


class UserUpdate(BaseModel):
    username: Optional[str]
    title: Optional[str]
    description: Optional[str]
    company_url: Optional[str]
    notification_email: Optional[str]
    manufacture_address: Optional[str]
    full_name: Optional[str]


class UserDelete(BaseModel):
    id: int
    delete_time: datetime
