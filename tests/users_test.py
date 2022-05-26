import unittest
from fastapi.testclient import TestClient
from routes.main import app
from fastapi import status
from schemas.register_user_response import CreateUserResponse
from pydantic import ValidationError


class TestCreateUser(unittest.TestCase):


    client = TestClient(app)
        
        
    def test_create_user_right_way(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79120347221", 
                                                        "name": "Alex"})
        assert res.status_code == status.HTTP_201_CREATED
        res_data = res.json()
        try:
            CreateUserResponse(**res_data)
        except Exception as create_user_schema_error:
            print(f"Test create user right way schema error: {create_user_schema_error}")
        assert res_data['email'] == "admin@mail.com"
        assert res_data['phone_number'] == "+79120347221"
        assert res_data['name'] == "Alex"

    def test_create_user_wrong_email(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "something", 
                                                        "password": "1234353", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "John"})
        except Exception as wrong_email_error:
            assert type(wrong_email_error) == ValidationError
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_user_no_email(self) -> None:
        try:
            res = self.client.post("/users/register", json={ 
                                                        "password": "1234353", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "John"
                                                        })
        except Exception as no_email_error:
            assert type(no_email_error) == ValidationError
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_user_no_phone_number(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "something", 
                                                        "password": "1234353", 
                                                        "name": "John"})
        except Exception as no_phone_number_error:
            assert type(no_phone_number_error) == ValidationError
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_user_no_password(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "something", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "John"})
        except Exception as no_password_error:
            assert type(no_password_error) == ValidationError
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_create_user_no_name(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "something", 
                                                        "password": "1234353", 
                                                        "phone_number": "+79111147221", 
                                                        })
        except Exception as no_name_error:
            assert type(no_name_error) == ValidationError
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
            