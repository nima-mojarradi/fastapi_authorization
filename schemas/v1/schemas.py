from pydantic import BaseModel, EmailStr, constr, validator
from fastapi.exceptions import HTTPException


class UserSignUp(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password1: str
    password2: str

    @validator('password2')
    def check_passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('Passwords do not match')
        return v


class UserResponse(BaseModel):
    username: str


class UserLogin(BaseModel):
    username: str
    password: str
