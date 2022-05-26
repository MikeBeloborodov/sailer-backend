from sqlalchemy.orm import Session
from schemas.register_user_request import CreateUserRequest
from database.models import User
from fastapi import HTTPException, status

def handle_register_new_user(register_data: CreateUserRequest, db: Session):
    try:
        user_to_save = User(**register_data.dict())
        db.add(user_to_save)
        db.commit()
        db.refresh(user_to_save)
    except Exception as execution_error:
        print(f"[!!] Execution error occured while saving user to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    return user_to_save