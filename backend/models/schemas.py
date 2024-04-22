""" model.py is used for db ORM, whereas schemas.py is used for data validation for fastapi (using pydantic) """
# from typing import Union
from pydantic import BaseModel, UUID4
import datetime

class ProductBase(BaseModel):
    barcode: str

class ProductRead(ProductBase):
    id: UUID4
    created_at: datetime.datetime

    class Config:
        orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[ProductRead] = []

#     class Config:
#         orm_mode = True
