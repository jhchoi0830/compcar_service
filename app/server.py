# import fastapi modules
from fastapi import FastAPI, HTTPException

# import model
from models.usedCarModel import UsedCar
from models.userModel import User

# import routers
from endpoints import carRoutes, userRoutes

app = FastAPI()

# connect router with endpoints
app.include_router(carRoutes.router)
app.include_router(userRoutes.router)
