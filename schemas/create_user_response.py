from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class CreateUserResponse(BaseModel):
    created_at: datetime
    updated_at: datetime
    email: EmailStr
    phone: str
    name: str
    user_id: int
    user_credits: float
    avatar: Optional[str]