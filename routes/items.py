from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from database.database_logic import get_db
from schemas.register_item_request import RegisterItemRequest
from schemas.register_item_response import RegisterItemResponse
from handles.item_handles import handle_register_new_item
from authentication import oauth

router = APIRouter(
    prefix="/items",
    tags=["Items interaction"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterItemResponse)
def register_new_item(register_item_data: RegisterItemRequest,
                    user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    return handle_register_new_item(register_item_data, user_id, db)


