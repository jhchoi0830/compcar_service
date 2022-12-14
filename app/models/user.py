# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel
from typing import Optional, List


class FavCar(BaseModel):
    make: str
    model: str
    madeYear: str


class User(BaseModel):
    email: str
    password: str
    favouriteCar: Optional[List[FavCar]] = None
