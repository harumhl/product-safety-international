from dotenv import load_dotenv
load_dotenv()

from typing import Union
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.init import get_db
from db import crud
from models import model
from models import schemas

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

@app.get("/products/{product_id}", response_model=schemas.ProductRead)
def get_product_by_id(product_id: str, db: Session = Depends(get_db)) -> model.Product:
    return crud.get_product_by_id(db, product_id)