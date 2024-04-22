from sqlalchemy.orm import Session
from models.model import Product

def get_products(db: Session): # TODO delete
    return db.query(Product).all()

def get_product_by_id(db: Session, id: str):
    # get() may not query from db
    return db.query(Product).filter(Product.id == id).first()

def get_product_by_barcode(db: Session, barcode: str):
    # get() may not query from db
    return db.query(Product).filter(Product.barcode == barcode).all()
