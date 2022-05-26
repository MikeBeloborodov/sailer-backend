import unittest
from fastapi.testclient import TestClient
from routes.main import app
from schemas.message import Message
from fastapi import status

class TestCreateUser(unittest.TestCase):

    client = TestClient(app)

    def test_root_response_code(self) -> None:
        res = self.client.get("/")
        assert res.status_code == status.HTTP_200_OK

    def test_response_message(self) -> None:
        res = self.client.get("/")
        assert res.json() == Message(message="Welcome to Sailer API.")
        