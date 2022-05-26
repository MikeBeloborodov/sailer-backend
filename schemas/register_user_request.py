from curses.ascii import HT
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class CreateUserRequest(BaseModel):
    email: EmailStr
    phone: str
    name: str
    avatar: Optional[HttpUrl]
