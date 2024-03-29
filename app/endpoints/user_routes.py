from fastapi import FastAPI, HTTPException, APIRouter, status, Depends, Request
from app.models.user import User, Settings
from app.models.hashing import Hash
from fastapi.middleware.cors import CORSMiddleware
from app.services.connect import user_collection
from app.services.database import register_user, login_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from bson.objectid import ObjectId



router = APIRouter()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post('/api/user/register')
async def create_user(request:User):
    if await register_user(request):
        return {"res":"created"}
    return {"message":"ID not created", "status-code":"Error Code 404"}


@router.post('/api/user/login')
async def login(request :User, Authorize: AuthJWT = Depends()):
    user = await login_user(request)
    user_id = str(user["_id"])
    if user:
        access_token = Authorize.create_access_token(subject=user["email"])
        refresh_token = Authorize.create_refresh_token(subject=user["email"])
        Authorize.set_access_cookies(access_token)
        Authorize.set_refresh_cookies(refresh_token)
        return {
            "res":"Successfully login",
            "userID":user_id
            }
    return {"res":"coudln't find"}


@router.post('/api/user/refresh')
async def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    Authorize.set_access_cookies(new_access_token)
    return {"res":"The token has been refresh"}


@router.delete('/api/user/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    Authorize.unset_jwt_cookies()
    return {"res":"Successfully logout"}


@router.get('/api/user/protected')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}