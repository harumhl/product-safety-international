from sqlalchemy.orm import Session
from models.model import Product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    # return db.query(Product).offset(skip).limit(limit).all()
    return db.query(Product).all()
