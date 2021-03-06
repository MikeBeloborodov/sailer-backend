from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from authentication import oauth
from typing import List
from database.database_logic import get_db
from schemas.item_schemas.register_item_request import RegisterItemRequest
from schemas.item_schemas.register_item_response import RegisterItemResponse
from schemas.item_schemas.get_item_response import GetItemResponse
from schemas.item_schemas.delete_item_response import DeleteItemResponse
from handles.item_handles import *

router = APIRouter(
    prefix="/items",
    tags=["Items interaction"]
)


# register item
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterItemResponse)
def register_new_item(register_item_data: RegisterItemRequest,
                    user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    return handle_register_new_item(register_item_data, user_id, db)


# get all items
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GetItemResponse])
def get_all_items(user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    return handle_get_all_items(user_id, db)


# get item by id
@router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=GetItemResponse)
def get_item_by_id(item_id: int,
                user_id: int = Depends(oauth.get_current_user),
                db: Session = Depends(get_db)):
    return handle_get_item_by_id(item_id, user_id, db)


# delete item by id
@router.delete("/{item_id}", status_code=status.HTTP_200_OK, response_model=DeleteItemResponse)
def delete_item_by_id(item_id: int,
                user_id: int = Depends(oauth.get_current_user),
                db: Session = Depends(get_db)):
    return handle_delete_item_by_id(item_id, user_id, db)

