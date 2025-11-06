from devopsproject.db import db

def get() -> list[dict]:
    return db.get_users()
