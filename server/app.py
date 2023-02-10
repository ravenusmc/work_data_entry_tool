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
                    post_data['ieNumber'], post_data['password'])
        hashed = db.encrypt_pass(post_data)
        user_created = db.insert(user, hashed)
        print('DONE')
        return jsonify('5')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        ieNumber = post_data['ieNumber']
        password = post_data['password']
        login_values = {}
        # Checking to see if the user is in the database
        login_flag, not_found, password_no_match, user = db.check(
            ieNumber, password)
        login_values['login_flag'] = login_flag
        login_values['Not_found'] = not_found
        login_values['Password_no_match'] = password_no_match
        login_values['user'] = user
    return jsonify(login_values)

@app.route('/locateAction', methods=['GET', 'POST'])
def locateAction():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        data = []
        action_found, action_id = db.locateAction(post_data)
        if action_found == 'None':
            data.append(action_found)
        else:
            data.append(action_found)
            data.append(action_id)
    return jsonify(data)

# May need to get rid of methods here and only use post
@app.route('/submitActionToDatabase', methods=['GET', 'POST'])
def submitActionToDatabase():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        db.submitAction(post_data)
    return jsonify('5')

@app.route('/submitMissingActionToDatabase', methods=['GET', 'POST'])
def submitMissingActionToDatabase():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        action_found = db.addMissingActionToDb(post_data)
    return jsonify('5')






if __name__ == '__main__':
    app.run()