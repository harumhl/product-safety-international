## How to Install

1. (Optional) Create a virtual environment
    1. Create with `python -m venv psi-venv`
    1. Activate with `source psi-venv/bin/activate`
1. Install dependencies with `pip install -r requirements.txt`

## How to Run

1. Update `.env` file accordingly
1. (If applicable) Activate the virtual environment `source psi-venv/bin/activate`
1. Run the app with `uvicorn main:app --reload`
1. Access `http://127.0.0.1:8000`

1. `http://127.0.0.1:8000/docs` for Swagger doc
1. `http://127.0.0.1:8000/redoc` for ReDoc