from json import JSONDecoder
import unittest
from fastapi.testclient import TestClient
from routes.main import app
from fastapi import status
from schemas.register_user_response import RegisterUserResponse
from schemas.login_user_response import LoginUserResponse
from database.database_logic import get_db
from tests.database_for_tests import override_get_db
from utils_for_tests import delete_test_user


class TestUsers(unittest.TestCase):


    app.dependency_overrides[get_db] = override_get_db


    client = TestClient(app)


    def test_register_user_right_way(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79120347221", 
                                                        "name": "Alex"})
        
        assert res.status_code == status.HTTP_201_CREATED
        res_data = res.json()
        RegisterUserResponse(**res_data)
        assert res_data['email'] == "admin@mail.com"
        assert res_data['phone_number'] == "+79120347221"
        assert res_data['name'] == "Alex"
        delete_test_user("admin@mail.com")


    def test_register_user_wrong_email(self) -> None:
        res = self.client.post("/users/register", json={"email": "something", 
                                                        "password": "1234353", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "John"})

        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_no_email(self) -> None:
        res = self.client.post("/users/register", json={ 
                                                    "password": "1234353", 
                                                    "phone_number": "+79111147221", 
                                                    "name": "John"
                                                    })
        
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_no_phone_number(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                    "password": "1234353", 
                                                    "name": "John"})

        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_no_password(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                    "phone_number": "+79111147221", 
                                                    "name": "John"})
        
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_no_name(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                    "password": "1234353", 
                                                    "phone_number": "+79111147221", 
                                                    })
        
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_empty_email(self) -> None:
        res = self.client.post("/users/register", json={"email": "", 
                                                    "password": "1234353", 
                                                    "phone_number": "+79111147221",
                                                    "name": "John" 
                                                    })
        
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_empty_password(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                    "password": "", 
                                                    "phone_number": "+79111147221", 
                                                    "name": "John"
                                                    })
        
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_empty_phone_number(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                    "password": "admin", 
                                                    "phone_number": "", 
                                                    "name": "John"
                                                    })
        
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_register_user_empty_name(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                    "password": "admin", 
                                                    "phone_number": "+79111147221", 
                                                    "name": ""
                                                    })
        
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_login_user_wrong_email(self) -> None:
        res = self.client.get("/users/login", json={"email": "aadmin@mail.com", "password": "admin"})
        assert res.status_code == status.HTTP_403_FORBIDDEN


    def test_login_user_wrong_password(self) -> None:
        res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "aadmin"})
        assert res.status_code == status.HTTP_403_FORBIDDEN


    def test_login_user_no_password(self) -> None:
        res = self.client.get("/users/login", json={"email": "admin@mail.com"})
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_login_user_no_email(self) -> None:
        res = self.client.get("/users/login", json={"password": "admin"})
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    def test_login_user_right_way(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79120347221", 
                                                        "name": "Alex"})
        res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
        delete_test_user("admin@mail.com")
        res_data = res.json()
        print(res_data)
        assert res.status_code == status.HTTP_200_OK
        LoginUserResponse(**res_data)
        assert res_data['token_type'] == "bearer"
