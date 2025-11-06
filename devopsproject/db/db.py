import mariadb
import os

db_config = {
    "host": os.environ.get("DEVOPS_DB_HOST", "localhost"),
    "port": int(os.environ.get("DEVOPS_DB_PORT", 3306)),
    "user": os.environ.get("DEVOPS_DB_USER", "devops"),
    "password": os.environ.get("DEVOPS_DB_PASSWORD", "password"),
    "database": os.environ.get("DEVOPS_DB_DATABASE", "devops"),
}

conn: mariadb.Connection

def connect() -> None:
    global conn
    conn = mariadb.connect(**db_config)

def disconnect() -> None:
    if conn:
        conn.close()

def init() -> None:
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)

def get_users() -> list[dict]:
    query = "SELECT id, name, email, password FROM users"
    with conn.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    return [data_to_user(*result) for result in results]

def get_user(id: int) -> dict | None:
    query = "SELECT id, name, email, password FROM users WHERE id = ? LIMIT 1"
    values = (id,)
    with conn.cursor() as cursor:
        cursor.execute(query, values)
        results = cursor.fetchall()
    if len(results) > 0:
        return data_to_user(*results[0])
    return None

def create_user(name: str, email: str, password: str) -> None:
    query = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)"
    values = (name, email, password)
    with conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()

def update_user(id: int, name: str, email: str, password: str) -> None:
    query = "UPDATE users SET name = ?, email = ?, password = ? WHERE id = ?"
    values = (name, email, password, id)
    with conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()

def delete_user(id: int) -> None:
    query = "DELETE FROM users WHERE id = ?"
    values = (id,)
    with conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()

def find_user_with_email(email: str) -> dict | None:
    query = "SELECT id, name, email, password FROM users WHERE email = ? LIMIT 1"
    values = (email,)
    with conn.cursor() as cursor:
        cursor.execute(query, values)
        results = cursor.fetchall()
    if len(results) > 0:
        return data_to_user(*results[0])
    return None

def data_to_user(id: int, name: str, email: str, password: str) -> dict:
    return {
        "id": id,
        "name": name,
        "email": email,
        "password": password
    }
