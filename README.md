# compcar_service

Backend requirements
python version : 3.9.13

fastapi : 0.85.2
uvicorn : 0.19.0
motor : 3.1.1
mongodb

## Setting with venv

Virtual environment setup
`py -3.9 -m venv venv`

Activate virtual environment
`venv\Scripts\activate`
deactivate: `deactivate`

Start fastAPI
`uvicorn app.server:app --reload` // app directory

## Setting with Docker

Build Docker
`docker build -t fastapi .`

Running container
`docker-compose up`
