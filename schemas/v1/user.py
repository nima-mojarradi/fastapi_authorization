from fastapi import FastAPI
from fastapi import APIRouter
import pymongo 
import os
import uuid
from pydantic import BaseModel, Field
import pymongo 
from typing import ClassVar
from bson import ObjectId
from fastapi_jwt_auth import AuthJWT


class UserSignUp(BaseModel):
   first_name : str
   last_name : str
   username : str
   password : str
   email : str
   phone_number : str


class UserLogin(BaseModel):
   username : str
   password : str

