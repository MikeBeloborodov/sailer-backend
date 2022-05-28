from sqlalchemy.orm import Session
from schemas.user_schemas.login_user_request import LoginUserRequest
from schemas.user_schemas.register_user_request import RegisterUserRequest
from schemas.user_schemas.update_user_request import UpdateUserRequest
from database.models import User
from fastapi import HTTPException, status
from passlib.context import CryptContext
from database.utils import *
from authentication import oauth
from schemas.user_schemas.login_user_response import LoginUserResponse
from datetime import datetime


def handle_register_new_user(register_user_data: RegisterUserRequest, db: Session):
    # check if password is less than 4 chars
    if len(register_user_data.password) < 4 :
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Password should be at least 4 characters.")
    
    # check if phone number is empty
    if len(register_user_data.phone_number) == 0:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Phone number is empty.")

    # check if name is empty
    if len(register_user_data.name) == 0:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Name is empty.")

    # check for same email address
    query_same_email = db.query(User).filter(User.email == register_user_data.email)
    user_same_email = query_same_email.first()

    if user_same_email:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="User with this email already registred.")

    # check for same phone number
    query_same_phone = db.query(User).filter(User.phone_number == register_user_data.phone_number)
    user_same_phone = query_same_phone.first()

    if user_same_phone:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="User with this phone number already registred.")

    # hash password
    try:
        pwd_context = CryptContext(schemes=['bcrypt'])
        register_user_data.password = pwd_context.hash(register_user_data.password)
    except Exception as hash_error:
        print(f"[{time_stamp()}][!!] Unable to hash new user password: {hash_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")
    
    # save user to db
    try:
        user_to_save = User(**register_user_data.dict())
        db.add(user_to_save)
        db.commit()
        db.refresh(user_to_save)
    except Exception as execution_error:
        print(f"[{time_stamp()}][!!] Execution error occured while saving user to db: {execution_error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

    return user_to_save


def handle_login_user(login_data: LoginUserRequest, db: Session):
     # retrieve user from db
    try:
        user_query = db.query(User).filter(User.email == login_data.email)
        found_user = user_query.first()
    except Exception as user_validation_error:
        print(f"[{time_stamp()}][!!] Error occured during user search in db: {user_validation_error.username}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database internal error during user search")

    if not found_user:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Wrong credentials.")
    
    # then we check if stored hashed password and given password are the same
    pwd_context = CryptContext(schemes=['bcrypt'])
    if not pwd_context.verify(login_data.password, found_user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Wrong credentials.")

    # if everything is okay we send data back
    access_token = oauth.create_access_token(data = {"user_id" : found_user.user_id})

    return LoginUserResponse(access_token=access_token, token_type="bearer")


def handle_update_user_by_id(user_to_update_id: int, 
                            user_update_data: UpdateUserRequest, 
                            user_id: int, 
                            db: Session):
    # check if update_data is empty
    if check_if_dict_is_empty(user_update_data.dict()):
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail="You are sending an empty update, or an update with keys that you do not have access to.")
    
    try:
        # get user with this id from db
        user_to_update_query = db.query(User).filter(User.user_id == user_to_update_id)
        user_to_update = user_to_update_query.first()
    except Exception as db_error:
        print(f"[!!] DB error occured: {db_error}")

    # check if it exists
    if not user_to_update:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User with this id does not exist")
    
    # check if user trying to update has the same id
    if user_to_update.user_id != user_id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="No access")

    # compile update payload
    update_payload = user_update_data.dict()
    update_payload['updated_at'] = datetime.now()
    update_payload = remove_empty_keys(update_payload)

    # if user updating password
    if check_if_dict_has_key(update_payload, 'password'):
        pwd_context = CryptContext(schemes=['bcrypt'])
        update_payload["password"] = pwd_context.hash(update_payload["password"])

    # if user updating phone number
    if check_if_dict_has_key(update_payload, 'phone_number'):
        same_phone_query = db.query(User).filter(User.phone_number == update_payload['phone_number'])
        same_phone_user = same_phone_query.first()
        if same_phone_user:
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="User with this phone number already exists.")
    
    # if user updating email
    if check_if_dict_has_key(update_payload, 'email'):
        same_email_query = db.query(User).filter(User.email == update_payload['email'])
        same_email_user = same_email_query.first()
        if same_email_user:
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="User with this phone email already exists.")
            
    # save updates to db
    try:
        user_to_update_query.update(update_payload, synchronize_session=False)
        db.commit()
        db.refresh(user_to_update)
    except Exception as update_error:
        print(f"[!!] DB error while updating user: {update_error}")
    
    return user_to_update



