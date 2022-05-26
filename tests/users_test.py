import unittest
from fastapi.testclient import TestClient
from routes.main import app
from fastapi import status
from schemas.register_user_response import CreateUserResponse

class TestCreateUser(unittest.TestCase):

    client = TestClient(app)
        
    def test_create_user_right_way(self) -> None:
        res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79120347221", 
                                                        "name": "Alex"})
        print(res.json())
        assert res.status_code == status.HTTP_201_CREATED
        res_data = res.json()
        try:
            CreateUserResponse(**res_data)
        except Exception as create_user_schema_error:
            print("Test create user right way scheema error: " + create_user_schema_error)
        assert res_data['email'] == "admin@mail.com"
        assert res_data['phone_number'] == "+79120347221"
        assert res_data['name'] == "Alex"