from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class UpdateUserRequest(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]
    phone_number: Optional[str]
    name: Optional[str]
    avatar: Optional[HttpUrl]

    class Config:
        orm_mode = True
        