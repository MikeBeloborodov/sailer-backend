from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.utils import time_stamp
from database.models import Item
from schemas.register_item_request import RegisterItemRequest

def handle_register_new_item(register_item_data: RegisterItemRequest, user_id: int, db: Session):
    # save item to db
    try:
        item_to_save = Item(**register_item_data.dict(), owner_id=user_id)
        db.add(item_to_save)
        db.commit()
        db.refresh(item_to_save)
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occured while saving item to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    return item_to_save
