import pytest
import db_old

def test_get_user():
    assert db_old.get_user("hugo") == {"name" : "hugo", "email": "hugo@mail", "password":"123"}

def test_create_user_champs_vides():
    with pytest.raises(ValueError):
        db_old.create_user("", "", "")

def test_create_user_pas_chanps_valides():
    db_old.create_user("champsvalides", "champsvalides@mail", "123")

def test_create_user_password_echec_taille():
    with pytest.raises(ValueError):
        db_old.create_user("echectaille","echec_taille@mail", "12")
    
def test_create_user_password_taille_valide():
    db_old.create_user("taillevalide","taille_valide@mail","123")

def test_create_user_name_echec_number():
    with pytest.raises(ValueError):
        db_old.create_user("3","echec_number@mail","123")

def test_create_user_name_echec_special_character():
    with pytest.raises(ValueError):
        db_old.create_user("!","special_character@mail","123")

def test_create_user_name_echec_special_space():
    with pytest.raises(ValueError):
        db_old.create_user(" ","special_space@mail","123")

def test_create_user_name_echec_valide():
   db_old.create_user("echecvalide", "echec_valide@mail", "123")


def test_create_user_email_echec_identique():
    with pytest.raises(ValueError):
        db_old.create_user("romain","hugo@mail","123")


def test_create_user_email_echec_valide():
   db_old.create_user("dsti", "dsti@mail", "123")

def test_create_user_echec_verification_creation_bdd_deja_cree():
    with pytest.raises(ValueError):
        db_old.create_user("hugo","hugo@mail","123")

def test_create_user_echec_verification_creation_bdd_inexistant():
    with pytest.raises(ValueError):
        db_old.get_user("inexistant")

def test_create_user_reussite_verification_creation_bdd():
    db_old.create_user("test", "test@mail", "123")
    db_old.get_user("test")

def test_delete_user_existe_pas():
    with pytest.raises(ValueError):
        db_old.delete_user("inexistant")

def test_delete_user_existe():
    db_old.create_user("existe", "existe@mail", "123")
    db_old.delete_user("existe")

def test_delete_user_bein_supp():
    db_old.delete_user("hugo")
    with pytest.raises(ValueError):
        db_old.get_user("hugo")

def test_update_user_existe_pas():
    with pytest.raises(ValueError):
        db_old.update_user("testupdateexistepas", "nvtestupdateexiste", "nvtestupadteexiste@gmail", "nv123")
        
def  test_update_user_existe():
        db_old.create_user("existe", "existe@mail", "123")
        db_old.update_user("existe","newexiste","newexiste@mail", "new123")
        db_old.get_user("newexiste")


def test_update_user_modif_nom():
    db_old.create_user("pasmodif", "pasmodif@mail","123")
    db_old.update_user("pasmodif", "modif","pasmodif@mail","123" )
    user = db_old.get_user("modif")
    assert user["name"] == "modif"

def test_update_user_modif_email():
    db_old.update_user("modif","modif", "modif@mail", "123")
    user = db_old.get_user("modif")
    assert user["email"] == ("modif@mail")

def test_update_user_modif_password():
    db_old.update_user("modif","modif", "modif@mail", "modif123")
    user = db_old.get_user("modif")
    assert user["password"] == ("modif123")

def test_update_user_champs_vides_nom():
    db_old.create_user("pasmodifchampsvides", "pasmodifchampsvides@gmail", "123")
    with pytest.raises(ValueError):
        db_old.update_user("pasmodifchampsvides", "", "pasmodifchampsvides@gmail", "123")

def test_update_user_champs_vides_email():
    with pytest.raises(ValueError):
        db_old.update_user("pasmodifchampsvides", "pasmodifchampsvides", "", "123")

def test_update_user_champs_vides_password():
    with pytest.raises(ValueError):
        db_old.update_user("pasmodifchampsvides", "pasmodifchampsvides", "pasmodifchampsvides@gmail", "")

def test_update_user_name_echec_number():
    db_old.create_user("echecnumber","echec_number@mail","123")
    with pytest.raises(ValueError):
        db_old.update_user("echecnumber" ,"3","echec_number@mail","123")

def test_update_user_name_echec_special_character():
    db_old.create_user("echecspecialcharacter","special_character@mail","123")
    with pytest.raises(ValueError):
        db_old.update_user("echecspecialcharacter", "!","special_character@mail","123")

def test_create_user_name_echec_special_space():
    db_old.create_user("echecspecialspace","special_space@mail","123")
    with pytest.raises(ValueError):
        db_old.update_user("echecspecialspace", " ","special_space@mail","123")

def test_update_user_password_echec_taille():
    db_old.create_user("echectaille","echec_taille@mail", "123")
    with pytest.raises(ValueError):
        db_old.update_user("echectaille", "echectaille","echec_taille@mail", "12")
  
def test_update_user_email_echec_identique():
    db_old.create_user("emailidentique","emailidentique@mail","123")
    db_old.create_user("emaildifferent","emaildifferent@mail","123")
    with pytest.raises(ValueError):
        db_old.update_user("emaildifferent","emaildifferent","emailidentique@mail","123")

def test_update_user_echec_verification_creation_bdd_inexistant():
    with pytest.raises(ValueError):
        db_old.get_user("inexistant")

def test_update_user_reussite_verification_creation_bdd():
    db_old.create_user("salut", "salut@mail", "123")
    db_old.update_user("salut", "verif", "verif@mail", "1263")
    db_old.get_user("verif")

def test_get_renvoit_1_user_erreur():
    with pytest.raises(ValueError):
        db_old.get_user("personne")

def test_get_renvoit_1_user():
    db_old.create_user("testget", "testget@mail", "123")
    db_old.get_user("testget")

def test_get_renvoit_list_user_erreur():
     db_old.create_user("testgetlist", "testgetlist@mail", "123")
     db_old.list_users()

