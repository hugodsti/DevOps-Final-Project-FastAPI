from devopsproject.db import db
import re

def get(id: int) -> dict:
    user = db.get_user(id)
    if not user:
        raise ValueError
    return user

def create(name: str, email: str, password: str) -> None:
    if name == "" or email == "" or password == "":
        raise ValueError
    if len(password)<3:
        raise ValueError
    if db.find_user_with_email(email):
        raise ValueError
    if not re.fullmatch(r"[A-Za-z]+", name):
        raise ValueError
    
    db.create_user(name, email, password)

def update(id: int, name: str, email: str, password: str) -> None:
    if not db.get_user(id):
        raise ValueError
    user_with_email = db.find_user_with_email(email)
    if user_with_email and id != user_with_email["id"]:
        raise ValueError
    if name == "" or email == "" or password == "":
        raise ValueError
    if not re.fullmatch(r"[A-Za-z]+", name):
        raise ValueError
    if len(password)<3:
        raise ValueError
    db.update_user(id, name, email, password)

def delete(id: int) -> None:
    if not db.get_user(id):
        raise ValueError
    db.delete_user(id)
    if db.get_user(id):
        raise ValueError
    

