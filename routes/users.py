from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.register_user_request import CreateUserRequest
from schemas.register_user_response import CreateUserResponse
from handles.user_handles import handle_register_new_user
from database.database_logic import get_db


router = APIRouter(
    prefix="/users",
    tags=["User interaction"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=CreateUserResponse)
def register_new_user(register_data: CreateUserRequest,
                    db: Session = Depends(get_db)):
    return handle_register_new_user(register_data, db)