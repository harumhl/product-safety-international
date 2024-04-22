from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from db.init import ModelBase

class Product(ModelBase):
    __tablename__ = "products"
    id = Column(UUID, primary_key=True)
    barcode = Column(String)
    created_at = Column(DateTime)
