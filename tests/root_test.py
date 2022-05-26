import unittest
from fastapi.testclient import TestClient
from routes.main import app

class TestCreateUser(unittest.TestCase):

    client = TestClient(app)

    def test_root_response_code(self) -> None:
        res = self.client.get("/")
        assert res.status_code == 200

    def test_response_message(self) -> None:
        res = self.client.get("/")
        assert res.json() == {"Message": "Welcome to Sailer API."}