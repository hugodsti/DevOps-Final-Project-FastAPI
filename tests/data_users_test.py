import pytest

from devopsproject.db import db
from devopsproject.data import users


@pytest.fixture(autouse=True)
def mock_db(monkeypatch: pytest.MonkeyPatch):
    data = {
        1: { "id": 1, "name": "Test", "email": "test@localhost", "password": "123" }
    }

    def mock_get_users():
        return list(data.values())
    monkeypatch.setattr(db, "get_users", mock_get_users)


class TestUsersGet():
    def test_get_users(self):
        assert users.get() == [{ "id": 1, "name": "Test", "email": "test@localhost", "password": "123" }]
