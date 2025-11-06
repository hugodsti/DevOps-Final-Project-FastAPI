from flask import Flask, render_template, request, redirect, url_for, abort
import db_old

app = Flask(__name__)

@app.get('/')
def index():
    return render_template("index.html", users=db_old.list_users())

@app.get('/api/users')
def get_all_users():
    return db_old.list_users()

@app.post('/api/user')
def new_user():
    username=request.form.get("username")
    email=request.form.get("email")
    password=request.form.get("password")
    db_old.create_user(username, email, password)
    return redirect(url_for("index"))

@app.post('/api/user/<username>/update')
def update_user(username):
    new_username=request.form.get("new_username")
    new_email=request.form.get("new_email")
    new_password=request.form.get("new_password")
    db_old.update_user(username, new_username, new_email, new_password)
    return redirect(url_for("index"))

@app.get('/api/user/<username>')
def get_user(username):
    return db_old.get_user(username)

@app.get('/api/user/<username>/delete')
def delete_user (username):
    db_old.delete_user(username)
    return redirect(url_for("index"))


# # --- Base de données temporaire en mémoire ---
# USERS = {
#     1: {"name": "Hugo", "email": "hugo@example.com", "password": "1234"}
# }
# NEXT_ID = 2

# # ----- ROUTES PRINCIPALES -----

# # Accueil : liste des utilisateurs
# @app.get('/')
# def index():
#     return render_template('index.html', mode='list', users=USERS)

# # Formulaire de création
# @app.get('/users/new')
# def new_user():
#     return render_template('index.html', mode='new')

# # Action de création (POST)
# @app.post('/users')
# def create_user():
#     global NEXT_ID
#     name = (request.form.get('name') or '').strip()
#     email = (request.form.get('email') or '').strip()
#     password = (request.form.get('password') or '').strip()

#     if not name or not email or not password:
#         return "Tous les champs sont requis", 400

#     uid = NEXT_ID
#     USERS[uid] = {"name": name, "email": email, "password": password}
#     NEXT_ID += 1
#     return redirect(url_for('index'))

# # Formulaire d’édition (GET)
# @app.get('/users/<int:user_id>/edit')
# def edit_user(user_id):
#     user = USERS.get(user_id)
#     if not user:
#         abort(404, "Utilisateur introuvable")
#     return render_template('index.html', mode='edit', user_id=user_id, user=user)

# # Action d’édition (POST)
# @app.post('/users/<int:user_id>/edit')
# def update_user(user_id):
#     user = USERS.get(user_id)
#     if not user:
#         abort(404, "Utilisateur introuvable")

#     name = (request.form.get('name') or '').strip()
#     email = (request.form.get('email') or '').strip()
#     old_password = request.form.get('old_password') or ''
#     new_password = request.form.get('new_password') or ''
#     confirm_password = request.form.get('confirm_password') or ''

#     # maj nom/email
#     if not name or not email:
#         return "Nom et e-mail requis", 400
#     user["name"] = name
#     user["email"] = email

#     # changement de mdp si demandé
#     if new_password or confirm_password:
#         if old_password != user["password"]:
#             return "Ancien mot de passe incorrect", 400
#         if new_password != confirm_password:
#             return "Les nouveaux mots de passe ne correspondent pas", 400
#         user["password"] = new_password

#     return redirect(url_for('index'))

# # Confirmation de suppression (GET)
# @app.get('/users/<int:user_id>/delete')
# def confirm_delete_user(user_id):
#     user = USERS.get(user_id)
#     if not user:
#         abort(404, "Utilisateur introuvable")
#     return render_template('index.html', mode='delete', user_id=user_id, user=user)

# # Action de suppression (POST)
# @app.post('/users/<int:user_id>/delete')
# def delete_user(user_id):
#     USERS.pop(user_id, None)
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
