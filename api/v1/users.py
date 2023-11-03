from schemas.v1.users import UserLogin, UserSignUp
# from main import collection
from bson import ObjectId
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from db.db import users_collection
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
import json
import asyncio


user_router = APIRouter(tags=["users"], prefix="/users")


@user_router.post("/signup")
async def user_signup(user:UserSignUp):
    print(user)
    print("1"*100)
    user_dictionary=jsonable_encoder(user)
    signedup_user = await users_collection.insert_one(user_dictionary)
    return Response({'user_id':signedup_user})
   
@user_router.post('/login')
def login_user(user:UserLogin):
    users = list(users_collection.find({}))
    for user in users:
        if (user['username']==user.username) and (user['password']==user.password):
            return user


