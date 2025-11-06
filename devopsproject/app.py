import os
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.parent))


from flask import Flask, abort, jsonify, render_template, request, Response

from devopsproject.db import db
from devopsproject.data import user, users


app = Flask(__name__)


@app.get("/")
def index() -> str:
    return render_template('index.html', users=users.get())

@app.get("/api/ready")
def api_ready()->Response:
    return jsonify()

@app.get('/api/users')
def api_get_users() -> Response:
    return jsonify(users.get())

@app.get('/api/user/<int:id>')
def api_get_user(id: int) -> Response:
    try:
        return jsonify(user.get(id))
    except:
        abort(400)

@app.post('/api/user')
def api_create_user() -> Response:
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    password = request.args.get('password', '')
    try:
        user.create(name, email, password)
        return jsonify()
    except:
        abort(400)

@app.put('/api/user/<int:id>')
def api_update_user(id: int) -> Response:
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    password = request.args.get('password', '')
    try:
        user.update(id, name, email, password)
        return jsonify()
    except:
        abort(400)

@app.delete('/api/user/<int:id>')
def api_delete_user(id: int) -> Response:
    try:
        user.delete(id)
        return jsonify()
    except:
        abort(400)


if __name__ == "__main__":
    db.connect()
    db.init()
    app.run(
        host=os.environ.get("DEVOPS_APP_HOST", "localhost"),
        port=int(os.environ.get("DEVOPS_APP_PORT", 5000)),
    )
    db.disconnect()
