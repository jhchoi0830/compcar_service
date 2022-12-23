from app.models.used_car import UsedCar
from app.models.user import User
from app.models.kijiji_car import KijijiCar
from app.services.connect import car_collection, kijiji_car_collection
from app.services.connect import user_collection
from app.models.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, status, HTTPException
from app.models.jwttoken import create_access_token



async def fetch_all_cars() -> list:
    cars = []
    cursor = car_collection.find({})
    async for document in cursor:
        cars.append(UsedCar(**document))
    return cars


async def fetch_kijiji_cars() -> list:
    cars = []
    cursor = kijiji_car_collection.find({})
    async for document in cursor:
        cars.append(KijijiCar(**document))
    return cars


async def fetch_car_by_maker(maker: str) -> list:
    cars = []
    cursor = car_collection.find({"maker":maker})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_model(model: str) -> list:
    cars = []
    cursor = car_collection.find({"model":{'$regex': '.*'+ model + '.*'}})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_color(color: str) -> list:
    cars = []
    cursor = car_collection.find({"color":color})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_year(year: int) -> list:
    cars = []
    cursor = car_collection.find({"madeYear":year})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_mileage(id: int) -> list:
    cars = []
    cursor = car_collection.find({"mileage": {'$gt':(id-1)*50000,'$lt':id*50000}})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_price(id: int) -> list:
    cars = []
    cursor = car_collection.find({"price.price": {'$gt':(id-1)*10000,'$lt':id*10000} })
    async for document in cursor:
        cars.append(document)
    return cars

async def register_user(request:User):
    hashed_pass = Hash.get_hash_password(request.password)
    user_object = dict(request)
    user_object["password"] = hashed_pass
    user = await user_collection.insert_one(user_object)
    return user

async def login_user(request:OAuth2PasswordRequestForm = Depends()):
    user = await user_collection.find_one({"email":request.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.username} username')
    if not Hash.verify_password(request.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
    access_token = create_access_token(data={"sub": user["email"] })
    return {"access_token": access_token, "token_type": "bearer"}

