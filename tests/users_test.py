from datetime import datetime
import unittest
from fastapi.testclient import TestClient
from fastapi import status
from routes.main import app
from schemas.user_schemas.register_user_response import RegisterUserResponse
from schemas.user_schemas.login_user_response import LoginUserResponse
from database.database_logic import get_db
from schemas.user_schemas.update_user_response import UpdateUserResponse
from tests.database_for_tests import override_get_db
from tests import utils_for_tests


class TestUsers(unittest.TestCase):


    app.dependency_overrides[get_db] = override_get_db


    client = TestClient(app)


    def test_register_user_right_way(self) -> None:
        try:
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
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_wrong_email(self) -> None:
        try: 
            res = self.client.post("/users/register", json={"email": "something", 
                                                            "password": "1234353", 
                                                            "phone_number": "+79111147221", 
                                                            "name": "John"})

            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_no_email(self) -> None:
        try:
            res = self.client.post("/users/register", json={ 
                                                        "password": "1234353", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "John"
                                                        })
            
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_no_phone_number(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "1234353", 
                                                        "name": "John"})

            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_no_password(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "John"})
            
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_no_name(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "1234353", 
                                                        "phone_number": "+79111147221", 
                                                        })
            
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_empty_email(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "", 
                                                        "password": "1234353", 
                                                        "phone_number": "+79111147221",
                                                        "name": "John" 
                                                        })
            
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_empty_password(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "John"
                                                        })
            
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_empty_phone_number(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "", 
                                                        "name": "John"
                                                        })
            
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_empty_name(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79111147221", 
                                                        "name": ""
                                                        })
            
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_same_email(self) -> None:
        try:
            res_normal_email = self.client.post("/users/register", 
                                                    json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "Alex"
                                                        })
            
            assert res_normal_email.status_code == status.HTTP_201_CREATED

            res_same_email = self.client.post("/users/register", 
                                                    json={"email": "admin@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79112147221", 
                                                        "name": "Alex"
                                                        })

            assert res_same_email.status_code == status.HTTP_403_FORBIDDEN
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_register_user_same_phone(self) -> None:
        try:
            res_normal_phone = self.client.post("/users/register", 
                                                json={"email": "admin@mail.com", 
                                                    "password": "admin", 
                                                    "phone_number": "+79111147221", 
                                                    "name": "Alex"
                                                    })
        
            assert res_normal_phone.status_code == status.HTTP_201_CREATED

            res_same_phone = self.client.post("/users/register", 
                                                    json={"email": "admin2@mail.com", 
                                                        "password": "admin", 
                                                        "phone_number": "+79111147221", 
                                                        "name": "Alex"
                                                        })
                                                        
            assert res_same_phone.status_code == status.HTTP_403_FORBIDDEN
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_login_user_wrong_email(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})

            res = self.client.get("/users/login", json={"email": "aadmin@mail.com", "password": "admin"})
            assert res.status_code == status.HTTP_404_NOT_FOUND
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_login_user_wrong_password(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})

            res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "aadmin"})
            utils_for_tests.delete_test_user("admin@mail.com")
            assert res.status_code == status.HTTP_403_FORBIDDEN
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_login_user_no_password(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})

            res = self.client.get("/users/login", json={"email": "admin@mail.com"})
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_login_user_no_email(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})

            res = self.client.get("/users/login", json={"password": "admin"})
            assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()


    def test_login_user_right_way(self) -> None:
        try:
            res = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})

            res = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            res_data = res.json()
            assert res.status_code == status.HTTP_200_OK
            LoginUserResponse(**res_data)
            assert res_data['token_type'] == "bearer"
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()

    
    def test_update_user_right_way(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"email": "admin2@mail.com", 
                            "password": "admin2", 
                            "phone_number": "+79130347221", 
                            "name": "Kirill",
                            "avatar": "https://www.w3schools.com/howto/img_avatar.png"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_200_OK

            # test response data
            res_update_user_data = res_update_user.json()
            res_update_user_data_converted = UpdateUserResponse(**res_update_user_data)
            assert res_update_user_data_converted.email == "admin2@mail.com"
            assert res_update_user_data_converted.phone_number == "+79130347221"
            assert res_update_user_data_converted.name == "Kirill"
            assert res_update_user_data_converted.avatar == "https://www.w3schools.com/howto/img_avatar.png"

            # login user after changes
            res_login = self.client.get("/users/login", json={"email": "admin2@mail.com", "password": "admin2"})
            assert res_login.status_code == status.HTTP_200_OK

        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


    def test_update_user_only_email(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"email": "admin2@mail.com"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_200_OK

            # test response data
            res_update_user_data = res_update_user.json()
            res_update_user_data_converted = UpdateUserResponse(**res_update_user_data)
            assert res_update_user_data_converted.email == "admin2@mail.com"
            assert res_update_user_data_converted.phone_number == "+79120347221"
            assert res_update_user_data_converted.name == "Alex"
            assert res_update_user_data_converted.avatar == None

            # login user after changes
            res_login = self.client.get("/users/login", json={"email": "admin2@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK

        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


    def test_update_user_only_password(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"password": "admin2"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_200_OK

            # test response data
            res_update_user_data = res_update_user.json()
            res_update_user_data_converted = UpdateUserResponse(**res_update_user_data)
            assert res_update_user_data_converted.email == "admin@mail.com"
            assert res_update_user_data_converted.phone_number == "+79120347221"
            assert res_update_user_data_converted.name == "Alex"
            assert res_update_user_data_converted.avatar == None

            # login user after changes
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin2"})
            assert res_login.status_code == status.HTTP_200_OK

        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")



    def test_update_user_only_email(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"email": "admin2@mail.com"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_200_OK

            # test response data
            res_update_user_data = res_update_user.json()
            res_update_user_data_converted = UpdateUserResponse(**res_update_user_data)
            assert res_update_user_data_converted.email == "admin2@mail.com"
            assert res_update_user_data_converted.phone_number == "+79120347221"
            assert res_update_user_data_converted.name == "Alex"
            assert res_update_user_data_converted.avatar == None

            # login user after changes
            res_login = self.client.get("/users/login", json={"email": "admin2@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK

             # create another user to check same email error
            res_register_2 = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120343221", 
                                                            "name": "Alex"})

            assert res_register_2.status_code == status.HTTP_201_CREATED
            
            # update payload
            update_payload_2 = {"email": "admin@mail.com"}

            # test response status code if this email already exists
            res_update_user_2 = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload_2)
            assert res_update_user_2.status_code == status.HTTP_403_FORBIDDEN


        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


    def test_update_user_only_phone_number(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"phone_number": "+79120347321"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_200_OK

            # test response data
            res_update_user_data = res_update_user.json()
            res_update_user_data_converted = UpdateUserResponse(**res_update_user_data)
            assert res_update_user_data_converted.email == "admin@mail.com"
            assert res_update_user_data_converted.phone_number == "+79120347321"
            assert res_update_user_data_converted.name == "Alex"
            assert res_update_user_data_converted.avatar == None

            # login user after changes
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK

            # create another user to check same phone number error
            res_register_2 = self.client.post("/users/register", json={"email": "admin2@mail.com", 
                                                            "password": "admin2", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})

            assert res_register_2.status_code == status.HTTP_201_CREATED
            
            # update payload
            update_payload_2 = {"phone_number": "+79120347221"}

            # test response status code if this number already exists
            res_update_user_2 = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload_2)
            assert res_update_user_2.status_code == status.HTTP_403_FORBIDDEN


        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


    def test_update_user_only_name(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"name": "Sanya"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_200_OK

            # test response data
            res_update_user_data = res_update_user.json()
            res_update_user_data_converted = UpdateUserResponse(**res_update_user_data)
            assert res_update_user_data_converted.email == "admin@mail.com"
            assert res_update_user_data_converted.phone_number == "+79120347221"
            assert res_update_user_data_converted.name == "Sanya"
            assert res_update_user_data_converted.avatar == None

            # login user after changes
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK

        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


    def test_update_user_only_avatar(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"avatar": "https://www.w3schools.com/howto/img_avatar.png"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_200_OK

            # test response data
            res_update_user_data = res_update_user.json()
            res_update_user_data_converted = UpdateUserResponse(**res_update_user_data)
            assert res_update_user_data_converted.email == "admin@mail.com"
            assert res_update_user_data_converted.phone_number == "+79120347221"
            assert res_update_user_data_converted.name == "Alex"
            assert res_update_user_data_converted.avatar == "https://www.w3schools.com/howto/img_avatar.png"

            # login user after changes
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK

        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


    def test_update_user_restricted_keys(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED
            res_register_data = res_register.json()
            res_register_data_converted = RegisterUserResponse(**res_register_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"user_credits": 10000000,
                            "created_at": f"{datetime.now()}",
                            "updated_at": f"{datetime.now()}",
                            "user_id": 32}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


    def test_update_user_wrong_credentials(self) -> None:
        try:
            # create new user
            res_register = self.client.post("/users/register", json={"email": "admin@mail.com", 
                                                            "password": "admin", 
                                                            "phone_number": "+79120347221", 
                                                            "name": "Alex"})
            
            assert res_register.status_code == status.HTTP_201_CREATED

            # create another user
            res_register2 = self.client.post("/users/register", json={"email": "admin2@mail.com", 
                                                            "password": "admin2", 
                                                            "phone_number": "+79130347221", 
                                                            "name": "Alexa"})
            
            assert res_register2.status_code == status.HTTP_201_CREATED
            res_register2_data = res_register2.json()
            res_register2_data_converted = RegisterUserResponse(**res_register2_data)

            # login user
            res_login = self.client.get("/users/login", json={"email": "admin@mail.com", "password": "admin"})
            assert res_login.status_code == status.HTTP_200_OK
            res_login_data = res_login.json()
            login_data_converted = LoginUserResponse(**res_login_data)

            # get token to the header
            self.client.headers = {
                **self.client.headers,
                "Authorization": f"Bearer {login_data_converted.access_token}"}

            # update payload
            update_payload = {"email": "admin23@mail.com", 
                            "password": "admin23", 
                            "phone_number": "+79130357221", 
                            "name": "Kirill",
                            "avatar": "https://www.w3schools.com/howto/img_avatar.png"}

            # test response status code
            res_update_user = self.client.patch(f"/users/{res_register2_data_converted.user_id}", json=update_payload)
            assert res_update_user.status_code == status.HTTP_403_FORBIDDEN

        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user("admin23@mail.com")
            utils_for_tests.delete_test_user("admin2@mail.com")
            utils_for_tests.delete_test_user("admin@mail.com")


