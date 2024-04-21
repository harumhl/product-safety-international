## How to Install

1. Run `pip install -r requirements.txt`

## How to Run

1. Update `SQLALCHEMY_DATABASE_URL` in db/init.py accordingly
1. Run `uvicorn main:app --reload`
1. Access `http://127.0.0.1:8000`

1. `http://127.0.0.1:8000/docs` for Swagger doc
1. `http://127.0.0.1:8000/redoc` for ReDoc