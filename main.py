from fastapi import FastAPI
from api.v1.users import user_router 

app = FastAPI()
app.include_router(router=user_router, prefix="")









