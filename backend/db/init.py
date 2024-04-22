import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.environ.get('POSTGRESQL_URL') # postgres://[user]:[password]@[host]:[port]/[database]

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocalClass = sessionmaker(autocommit=False, autoflush=False, bind=engine)

ModelBase = declarative_base()

def get_db():
    db = SessionLocalClass()
    try:
        yield db
    finally:
        db.close()
