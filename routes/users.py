from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.user_schemas.register_user_request import RegisterUserRequest
from schemas.user_schemas.register_user_response import RegisterUserResponse
from schemas.user_schemas.update_user_request import UpdateUserRequest
from schemas.user_schemas.update_user_response import UpdateUserResponse
from handles.user_handles import *
from database.database_logic import get_db
from schemas.user_schemas.login_user_response import LoginUserResponse
from schemas.user_schemas.login_user_request import LoginUserRequest
from authentication import oauth


router = APIRouter(
    prefix="/users",
    tags=["User interaction"]
)


# register user
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterUserResponse)
def register_new_user(register_user_data: RegisterUserRequest,
                    db: Session = Depends(get_db)):
    return handle_register_new_user(register_user_data, db)


# login user
@router.get("/login", status_code=status.HTTP_200_OK, response_model=LoginUserResponse)
def login_user(login_data: LoginUserRequest,
                db: Session = Depends(get_db)):
    return handle_login_user(login_data, db)


# update user by id
@router.patch("/{user_to_update_id}", status_code=status.HTTP_200_OK, response_model=UpdateUserResponse)
def update_user_by_id(user_to_update_id: int,
                    user_update_data: UpdateUserRequest,
                    user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    return handle_update_user_by_id(user_to_update_id, user_update_data, user_id, db)


