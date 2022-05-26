from sqlalchemy.orm import Session
from schemas.register_user_request import CreateUserRequest

def handle_register_new_user(register_data: CreateUserRequest, db: Session):
    pass