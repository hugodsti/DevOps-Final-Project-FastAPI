import pytest

from devopsproject.db import db
from devopsproject.data import user


@pytest.fixture(autouse=True)
def mock_db(monkeypatch: pytest.MonkeyPatch):
    data = {
        1: { "id": 1, "name": "Test", "email": "test@localhost", "password": "123" }
    }

    def mock_get_user(id: int) -> dict | None:
        try:
            return data[id]
        except:
            return None
    monkeypatch.setattr(db, "get_user", lambda id: mock_get_user(id))

    def mock_create_user(name: str, email: str, password: str) -> None:
        id = len(data) + 1
        data[id] = { "id": id, "name": name, "email": email, "password": password }
    monkeypatch.setattr(db, "create_user", lambda name, email, password: mock_create_user(name, email, password))

    def mock_update_user(id: int, name: str, email: str, password: str) -> None:
        data[id] = { "id": id, "name": name, "email": email, "password": password }
    monkeypatch.setattr(db, "update_user", lambda id, name, email, password: mock_update_user(id, name, email, password))

    def mock_delete_user(id: int) -> None:
        del data[id]
    monkeypatch.setattr(db, "delete_user", lambda id: mock_delete_user(id))

    def mock_find_user_with_email(email: str) -> dict | None:
        for user in list(data.values()):
            if user["email"] == email:
                return user
        return None
    monkeypatch.setattr(db, "find_user_with_email", lambda email: mock_find_user_with_email(email))


class TestUserGet():
    def test_get_user(self):
        assert user.get(1) == { "id": 1, "name": "Test", "email": "test@localhost", "password": "123" }

    def test_get_non_existing_user(self):
        with pytest.raises(ValueError):
            user.get(255)


class TestUserCreate:
    def test_create_user(self):
        user.create("TestCreate", "testcreate@localhost", "123")
        assert user.get(2) == { "id": 2, "name": "TestCreate", "email": "testcreate@localhost", "password": "123" }

    def test_create_empty_name_user(self):
        with pytest.raises(ValueError):
            user.create("", "testcreateemptyname@localhost", "123")
    
    def test_create_user_name_echec_number(self):
        with pytest.raises(ValueError):
            user.create("3","echec_number@mail","123")
    
    def test_create_user_name_echec_special_character(self):
        with pytest.raises(ValueError):
            user.create("!","special_character@mail","123")
    
    def test_create_user_name_echec_valide(self):
        user.create("echecvalide", "echec_valide@mail", "123")

    def test_create_empty_email_user(self):
        with pytest.raises(ValueError):
            user.create("Test", "", "123")

    def test_create_empty_password_user(self):
        with pytest.raises(ValueError):
            user.create("Test", "testcreateemptypassword@localhost", "")
    
    def test_create_too_short_password_user(self):
        with pytest.raises(ValueError):
            user.create("echectaille", "echec_taille@mail", "12")
    
    def test_create_good_password_user(self):
        user.create("taillevalide","taille_valide@mail","123")

    def test_create_already_existing_email_user(self):
        with pytest.raises(ValueError):
            user.create("Test", "test@localhost", "123")

  


class TestUserUpdate:
    def test_update_user(self):
        user.update(1, "TestUpdateModified", "testupdatemodified@localhost", "123modified")
        assert user.get(1) == { "id": 1, "name": "TestUpdateModified", "email": "testupdatemodified@localhost", "password": "123modified" }

    def test_update_to_same_values_user(self):
        user.update(1, "TestUpdateModified", "testupdatemodified@localhost", "123modified")

    def test_update_non_existing_user(self):
        with pytest.raises(ValueError):
            user.update(255, "TestUpdate", "testupdatenonexisting@localhost", "123")

    def test_update_to_already_existing_email_user(self):
        user.create("TestUpdate", "testupdate@localhost", "123")
        with pytest.raises(ValueError):
            user.update(2, "TestUpdate", "test@localhost", "123")
    
    def test_update_user_modif_nom(self):
        user.update(1, "testupdate","test@localhost","123" )
        updated_user = user.get(1)
        assert updated_user["name"] == "testupdate"

    def test_update_user_modif_email(self):
        user.update(1, "test","testupdate@localhost","123" )
        updated_user = user.get(1)
        assert updated_user["email"] == "testupdate@localhost"

    def test_update_user_modif_password(self):
        user.update(1, "test","test@localhost","update123" )
        updated_user = user.get(1)
        assert updated_user["password"] == "update123"
    
    def test_update_user_champs_vides_nom(self):
        with pytest.raises(ValueError):
            user.update(1, "", "test@localhost", "123")

    def test_update_user_champs_vides_email(self):
        with pytest.raises(ValueError):
            user.update(1, "test", "", "123")
    
    def test_update_user_champs_vides_password(self):
        with pytest.raises(ValueError):
            user.update(1, "test", "test@localhost", "")
    
    def test_update_echec_username_with_number(self):
        with pytest.raises(ValueError):
            user.update(1, "3", "test@localhost", "123")

    def test_update_echec_username_with_special_character(self):
        with pytest.raises(ValueError):
            user.update(1, "!", "test@localhost", "123")

    def test_update_too_short_password_user(self):
        with pytest.raises(ValueError):
            user.update(1,"echectaille", "echec_taille@mail", "12")
    
    def test_update_good_password_user(self):
        user.update(1, "taillevalide","taille_valide@mail","123")


class TestUserDelete:
    def test_delete_user(self):
        user.delete(1)
        with pytest.raises(ValueError):
            user.get(1)

    def test_delete_non_existing_user(self):
        with pytest.raises(ValueError):
            user.delete(255)
