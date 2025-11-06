import re


users = {
    "hugo" : {"name" : "hugo", "email": "hugo@mail", "password":"123"},
    "romain" : {"name" : "romain", "email": "romain@mail", "password":"123"},
}

def get_user(name):
    if name not in users:
        raise ValueError
    return users[name]

def create_user(name, email, password):
    if name == "" or email == "" or password == "":
        raise ValueError
    if len(password)<3:
        raise ValueError
    if not re.fullmatch(r"[A-Za-z]+", name):
        raise ValueError
    
    for user in list(users.values()):
        if email == user["email"]:
            raise ValueError
    if name in users:
        raise ValueError
    

    users[name]= {"name": name, "email":email, "password":password}
    

def delete_user(name):
    if name not in users:
        raise ValueError
    
    del users[name]

def update_user(name, new_name, new_email, new_password):
    if name not in users:
        raise ValueError
    
    delete_user(name)
    create_user(new_name, new_email, new_password )

def list_users():
    return list(users.values())
