from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from authentication import oauth
from typing import List
from database.database_logic import get_db
from schemas.register_item_request import RegisterItemRequest
from schemas.register_item_response import RegisterItemResponse
from schemas.get_item_response import GetItemResponse
from handles.item_handles import handle_register_new_item
from handles.item_handles import handle_get_all_items

router = APIRouter(
    prefix="/items",
    tags=["Items interaction"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterItemResponse)
def register_new_item(register_item_data: RegisterItemRequest,
                    user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    return handle_register_new_item(register_item_data, user_id, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GetItemResponse])
def get_all_items(user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    return handle_get_all_items(user_id, db)


