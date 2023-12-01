from flask import g
from database.dataconn import get_db_conn
from flask import Flask
from flask_cors import CORS
from authent.auth import token_required

__version__ = '0.1.0'
api = Flask(__name__)
cors = CORS(api, resources={r"/profile/*": {"origins": "*"}})

@api.before_request
def before_request():
    g.db_conn = get_db_conn()

@api.teardown_request
def teardown_request(exception):
    db_conn = getattr(g, 'db_conn', None)
    if db_conn is not None:
        db_conn.close()
        del g._db_conn

@api.route('/profile/<id>')
@token_required
def my_profile(user, id):
    print(user)
    response_body = {
        "firstname": user['firstname'],
        "email": user['email'],
        "username": user['username'],
        "id": id
    }
    print(user)
    return response_body