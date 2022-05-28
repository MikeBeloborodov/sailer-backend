import unittest
from fastapi.testclient import TestClient
from fastapi import status
from routes.main import app
from schemas.user_schemas.login_user_response import LoginUserResponse
from schemas.item_schemas.register_item_response import RegisterItemResponse
from schemas.item_schemas.delete_item_response import DeleteItemResponse
from schemas.user_schemas.register_user_response import RegisterUserResponse
from database.database_logic import get_db
from tests.database_for_tests import override_get_db
from tests import utils_for_tests


class TestGetItems(unittest.TestCase):


    app.dependency_overrides[get_db] = override_get_db


    client = TestClient(app)


    test_items = [{
                    "title": "Old table for studying",
                    "description": "My old table that I used back in school.",
                    "price": 1500.50, 
                    "cathegory": "furniture",
                    "address": "Russia, Moscow, Lenina str. 32, 15",
                    "condition": "good",
                    "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                },
                {
                    "title": "New chair",
                    "description": "I bought this chair yesterday, but I don't need it anymore, because we move to another country.",
                    "price": 3254.10, 
                    "cathegory": "furniture",
                    "address": "Russia, Samara, Kirova str. 32, 12",
                    "condition": "new",
                    "photo": "https://m.media-amazon.com/images/I/71UUH5GgUUL._AC_SY679_.jpg"
                },
                {
                    "title": "Old radio",
                    "description": "My granny's old radio. It's broken...",
                    "price": 532.90, 
                    "cathegory": "electronics",
                    "address": "Russia, Novosibirsk, Samoilova str. 11, 4",
                    "condition": "broken",
                    "photo": "https://m.media-amazon.com/images/I/81KUQ9V7IlS._AC_SY355_.jpg"
                },
                {
                    "title": "Lenovo laptop",
                    "description": "My son used this laptop in school. Keyboard is a bit sticky.",
                    "price": 6500, 
                    "cathegory": "electronics",
                    "address": "Russia, Kirov, Bratskaya str. 12, 22",
                    "condition": "bad",
                    "photo": "https://m.media-amazon.com/images/I/81Fx0897k2L._AC_SX425_.jpg"
                },
                {
                    "title": "Beats headphones",
                    "price": 1200, 
                    "cathegory": "accessories",
                    "address": "Russia, Kaliningrad, Kustov str. 1, 43",
                    "condition": "medium",
                    "photo": "https://m.media-amazon.com/images/I/61fr+upASHL._AC_SY355_.jpg"
                },
                {
                    "title": "Samsung charger",
                    "price": 250, 
                    "cathegory": "accessories",
                    "address": "Russia, Pskov, Alarskaya str. 14, 22",
                    "condition": "good",
                    "photo": "https://m.media-amazon.com/images/I/31vspRFCgFL._AC_.jpg"
                },]

    def test_delete_item_by_id_right_way(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED
            register_user_res_data = register_res.json()
            register_user_res_converted_data = RegisterUserResponse(**register_user_res_data)

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # list to save id of items
            items_id = []

            # after that we register our items with a valid token
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            for item in self.test_items:
                register_item_res = self.client.post("/items/register", json=item)
                assert register_item_res.status_code == status.HTTP_201_CREATED
                register_item_res_data = register_item_res.json()
                register_item_res_data_converted = RegisterItemResponse(**register_item_res_data)
                items_id.append(register_item_res_data_converted.item_id)
            
            # check registered items status
            for item_id in items_id:
                res_get_item_by_id = self.client.get(f"/items/{item_id}")
                assert res_get_item_by_id.status_code == status.HTTP_200_OK

            # check delete status
            res_delete = self.client.delete(f"/items/{items_id[0]}")
            assert res_delete.status_code == status.HTTP_200_OK

            # check delete response content
            res_delete_data = res_delete.json()
            res_delete_converted_data = DeleteItemResponse(**res_delete_data)
            assert res_delete_converted_data.title == self.test_items[0]["title"]
            assert res_delete_converted_data.price == self.test_items[0]["price"]
            assert res_delete_converted_data.address == self.test_items[0]["address"]
            assert res_delete_converted_data.condition == self.test_items[0]["condition"]
            assert res_delete_converted_data.cathegory == self.test_items[0]["cathegory"]
            assert res_delete_converted_data.owner_id == register_user_res_converted_data.user_id
            assert res_delete_converted_data.deleted == True
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_delete_item_by_id_wrong_user(self):
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            print(RegisterUserResponse(**res_register.json()))

            # create another user
            res_register2 = self.client.post("/users/register", json={"email": "admin2@mail.com", 
                                                            "password": "admin2", 
                                                            "phone_number": "+79130347221", 
                                                            "name": "Alexa"})
            
            assert res_register2.status_code == status.HTTP_201_CREATED
            print(RegisterUserResponse(**res_register2.json()))

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            #assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            print(res_data)
            converted_login_res = LoginUserResponse(**res_data)

            # login with another user
            another_login_res = self.client.get("/users/login", json={"email": "admin2@mail.com", "password": "admin2"})
            assert another_login_res.status_code == status.HTTP_200_OK
            another_res_data = another_login_res.json()
            print(another_res_data)
            another_converted_login_res = LoginUserResponse(**another_res_data)
            
            # make sure that tokens are not the same
            assert converted_login_res.access_token != another_converted_login_res.access_token

            # list to save id of items
            items_id = []

            # after that we register our items with a valid token
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            for item in self.test_items:
                register_item_res = self.client.post("/items/register", json=item)
                assert register_item_res.status_code == status.HTTP_201_CREATED
                register_item_res_data = register_item_res.json()
                register_item_res_data_converted = RegisterItemResponse(**register_item_res_data)
                items_id.append(register_item_res_data_converted.item_id)
            
            # check registered items status
            for item_id in items_id:
                res_get_item_by_id = self.client.get(f"/items/{item_id}")
                assert res_get_item_by_id.status_code == status.HTTP_200_OK
            
            # change client header token
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {another_converted_login_res.access_token}"}
            
            # send delete request from another user
            delete_res = self.client.delete(f"/items/{items_id[0]}")
            assert delete_res.status_code == status.HTTP_403_FORBIDDEN
            
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin@mail.com")
            utils_for_tests.delete_test_user("admin2@mail.com")

