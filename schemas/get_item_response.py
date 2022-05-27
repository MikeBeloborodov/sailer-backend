from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional
from datetime import datetime
from enum import Enum


class CathegoryEnum(str, Enum):
    furniture = 'furniture'
    electronics = 'electronics'
    vehicles = 'vehicles'
    accessories = 'accessories'


class ConditionEnum(str, Enum):
    new = 'new'
    good = 'good'
    medium = 'medium'
    bad = 'bad'
    broken = 'broken'


class GetItemResponse(BaseModel):
    item_id: int
    created_at: datetime
    updated_at: datetime
    owner_id: int
    title: str
    description: Optional[str]
    price: float
    cathegory: CathegoryEnum
    address: str
    condition: ConditionEnum
    photo: Optional[HttpUrl]
    reserved: bool
    

    class Config:
        orm_mode = True
        