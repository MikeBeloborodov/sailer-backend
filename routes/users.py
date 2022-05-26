from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.register_user_request import RegisterUserRequest
from schemas.register_user_response import RegisterUserResponse
from handles.user_handles import handle_register_new_user, handle_login_user
from database.database_logic import get_db
from schemas.login_user_response import LoginUserResponse
from schemas.login_user_request import LoginUserRequest


router = APIRouter(
    prefix="/users",
    tags=["User interaction"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterUserResponse)
def register_new_user(register_data: RegisterUserRequest,
                    db: Session = Depends(get_db)):
    return handle_register_new_user(register_data, db)


@router.get("/login", status_code=status.HTTP_200_OK, response_model=LoginUserResponse)
def login_user(login_data: LoginUserRequest,
                    db: Session = Depends(get_db)):
    return handle_login_user(login_data, db)

