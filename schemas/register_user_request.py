from curses.ascii import HT
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str
    phone_number: str
    name: str
    avatar: Optional[HttpUrl]

    class Config:
        orm_mode = True