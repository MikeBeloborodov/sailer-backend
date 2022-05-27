from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime
from typing import Optional

class UpdateUserResponse(BaseModel):
    created_at: datetime
    updated_at: datetime
    email: EmailStr
    phone_number: str
    name: str
    user_id: int
    user_credits: float
    avatar: Optional[HttpUrl]

    class Config:
        orm_mode = True
        