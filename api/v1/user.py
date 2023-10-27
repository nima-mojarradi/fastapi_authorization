from schemas.v1 import user
# from main import collection
from bson import ObjectId
from fastapi import FastAPI, Depends
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from db.db import users_table
import json
from schemas.v1.user import UserLogin, UserSignUp
from fastapi_jwt_auth import AuthJWT
import asyncio
user_router = APIRouter(tags=["user"], prefix="/users")

@user_router.post('/signup')
async def create_user(user: UserSignUp):
    print(user)
    print("1"*100)
    created_user = asyncio.run ,users_table.insert_one(user.dict())
    return {'book_id':str(created_user)}


@user_router.post('/login')
def login_user(user:UserLogin,Authorize:AuthJWT=Depends()):
    users = list(users_table.find({}))
    for user in users:
        if (user['username']==user.username) and (user['password']==user.password):
            return user
