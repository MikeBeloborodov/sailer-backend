import unittest
from fastapi.testclient import TestClient
from fastapi import status
from routes.main import app
from schemas.user_schemas.login_user_response import LoginUserResponse
from schemas.item_schemas.register_item_response import RegisterItemResponse
from database.database_logic import get_db
from tests.database_for_tests import override_get_db
from tests import utils_for_tests


class TestRegisterItem(unittest.TestCase):


    app.dependency_overrides[get_db] = override_get_db


    client = TestClient(app)


    def test_register_item_right_way(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_201_CREATED
            register_item_res_data = register_item_res.json()
            RegisterItemResponse(**register_item_res_data)
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_no_title(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_no_description(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_201_CREATED
            register_item_res_data = register_item_res.json()
            RegisterItemResponse(**register_item_res_data)
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_no_price(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_no_cathegory(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_no_address(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_no_condition(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_no_photo(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_201_CREATED
            register_item_res_data = register_item_res.json()
            RegisterItemResponse(**register_item_res_data)
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_empty_title(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_empty_price(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": "", 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_empty_cathegory(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_empty_address(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_empty_condition(self):
        try: 
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_wrong_price(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": "15a00.50", 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_wrong_condition(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "furniture",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "somewhat good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_item_wrong_cathegory(self):
        try:
            # first of all we register user 
            register_res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            assert register_res.status_code == status.HTTP_201_CREATED

            # then we login user to get a token
            login_res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert login_res.status_code == status.HTTP_200_OK
            res_data = login_res.json()
            converted_login_res = LoginUserResponse(**res_data)

            # after that we register our item with a valid token
            register_item_payload = {
                                        "title": "Old table for studying",
                                        "description": "My old table that I used back in school.",
                                        "price": 1500.50, 
                                        "cathegory": "my cathegory",
                                        "address": "Russia, Moscow, Lenina str. 32, 15",
                                        "condition": "good",
                                        "photo": "https://opensooq-images.os-cdn.com/previews/700x0/d8/c8/d8c8126486b767c49b84a6eab4312247fb7dd498975c5b4beefa993668bb3ac5.jpg.jpg"
                                    }

            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {converted_login_res.access_token}"}
            register_item_res = self.client.post("/items/register", json=register_item_payload)
            assert register_item_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()



