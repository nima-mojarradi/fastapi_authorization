from schemas.v1.schemas import UserSignUp, UserLogin
from bson import ObjectId
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
import json
from db.db import RedisDB
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
# from util.jwt_handler import access_jwt, refresh_jwt, decode_access_token, decode_refresh_token
import httpx
user_router = APIRouter(tags=["users"], prefix="/users")

@user_router.post("/signup")
async def user_signup(user:UserSignUp):
    async with httpx.AsyncClient() as client:
        response = await client.post(f'http://127.0.0.1:8001/user/create', json=user.model_dump())
    if not user.check_passwords_match:
        raise HTTPException(status_code=400,detail="your password doesn't match to the password2")
    else:
        content = response.json()
        return content

@user_router.post('/login')
def login_user(user:UserLogin):
    print(user)
    print("1"*100)
    user_dictionary=dict(user)
    return Response(content=json.dumps(user_dictionary), media_type="application/json")

