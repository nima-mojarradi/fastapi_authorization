from fastapi import FastAPI
from fastapi import APIRouter
import pymongo 
import uuid
from pydantic import BaseModel, Field
import pymongo 
from bson import ObjectId
from api.v1.user import user_router
# from api.v1.user 

app = FastAPI()

# client=pymongo.MongoClient(host='127.0.0.1', port=27017)

app.include_router(prefix='', router=user_router)








