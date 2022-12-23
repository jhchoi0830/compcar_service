from fastapi import FastAPI, HTTPException, APIRouter, status, Depends
from app.models.user import User
from app.models.hashing import Hash
from app.models.oauth import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from app.services.connect import user_collection
from app.services.database import register_user, login_user
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter()


@router.post('/api/user/register')
async def create_user(request:User):
    if await register_user(request):
        return {"res":"created"}
    return {"res":"ID not created"}


@router.post('/api/user/login')
async def login(request:OAuth2PasswordRequestForm = Depends()):
    if await login_user(request):
        return {"res":"found"}
    return {"res":"coudln't find"}