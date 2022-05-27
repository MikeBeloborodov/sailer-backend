from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.utils import time_stamp
from database.models import Item
from schemas.register_item_request import RegisterItemRequest

def handle_register_new_item(register_item_data: RegisterItemRequest, user_id: int, db: Session):
    # check if title is is empty
    if len(register_item_data.title) == 0 :
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Title is empty")
    
    # check if address is empty
    if len(register_item_data.address) == 0:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Address is empty.")

    
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



def handle_get_all_items(user_id: int, db: Session):
    # execution check
    try:
        posts = (db.query(Item)
                    .all())
    except Exception as execution_error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                    detail="Could not retrieve data from DB")

    # availability check
    if not posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                                    detail="Items database is empty")
    
    # if ok return all posts
    return posts