import unittest
from fastapi.testclient import TestClient
from fastapi import status
from routes.main import app
from schemas.user_schemas.register_user_response import RegisterUserResponse
from schemas.user_schemas.login_user_response import LoginUserResponse
from database.database_logic import get_db
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
            assert res.status_code == status.HTTP_403_FORBIDDEN
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
            print(res_data)
            assert res.status_code == status.HTTP_200_OK
            LoginUserResponse(**res_data)
            assert res_data['token_type'] == "bearer"
        except Exception as error:
            raise error
        finally:
            utils_for_tests.delete_test_user()

