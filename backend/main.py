from typing import Union
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# from models.schemas import Item
from db.init import get_db
from db import crud

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

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)