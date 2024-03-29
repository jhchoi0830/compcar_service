# compcar_service

Backend requirements on local machine:

- python3: 3.9.13
- pip
- mongodb

# Install & Setup

### 1. Install required packages

```bash
pip install -r requirements.txt
```

### 2. Setting with venv

1. Virtual environment setup

```bash
py -3.9 -m venv venv

# If you have not setup alias, run:
python3 -m venv venv
```

2. Activate virtual environment

```bash
# For Windows
venv\Scripts\activate

# For Mac
source venv/bin/activate

# deactivate:
deactivate
```

# Usage

### Start fastAPI server

```bash
uvicorn app.server:app --reload
```

### Run server with Docker

1. Build Docker: `docker build -t fastapi .`
2. Running container: `docker-compose up`

### API Document

- http://localhost:8000/docs
- http://localhost:8000/redoc

## Tests

### How to run tests

- Required local server running

```bash
python -m pytest -v

# If you have not setup alias python3, run:
python3 -m pytest -v

# Run each test case:
python3 -m pytest -v <test case with path>
# Example:
python3 -m pytest -v tests/unit/endpoints/test_car_routes.py::test_get_root
```

# Deployment

- https://compcar-api.onrender.com/
  (Deployed by render(https://render.com/))
