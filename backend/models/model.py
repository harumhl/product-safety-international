from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from db.init import ModelBase

class Product(ModelBase):
    __tablename__ = "products"
    id = Column(UUID, primary_key=True)
    created_at = Column(DateTime)
