from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I created for the project
# from data import *
from db import *
from user import *


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        user = User(post_data['firstName'], post_data['lastName'], post_data['email'],
                    post_data['userName'], post_data['password'])
        hashed = db.encrypt_pass(post_data)
        # user_created = db.insert(user, hashed)
        # return jsonify(user_created)
        return jsonify('5')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         db = Connection()
#         post_data = request.get_json()
#         username = post_data['userName']
#         password = post_data['password']
#         login_values = {}
#         # Checking to see if the user is in the database
#         login_flag, not_found, password_no_match, user = db.check(
#             username, password)
#         login_values['login_flag'] = login_flag
#         login_values['Not_found'] = not_found
#         login_values['Password_no_match'] = password_no_match
#         login_values['user'] = user
#     return jsonify(login_values)


if __name__ == '__main__':
    app.run()