from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I created for the project
# from data import *
from db import *
from user import *
from analyze import *


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

@app.route('/submitMissingActionToDatabase', methods=['POST'])
def submitMissingActionToDatabase():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        db.submitMissingActionToDatabase(post_data)
    missing_action_submitted = True
    return jsonify(missing_action_submitted)

@app.route('/changeDynamicGraphs', methods=['POST'])
def changeDynamicGraphs():
    if request.method == 'POST':
        analyze = Analyze()
        post_data = request.get_json()
        data_container = []
        chart_data = analyze.get_graph_data_ienumber_by_action(post_data)
        chart_data_2 = analyze.get_graph_data_by_recruit_actions(post_data)
        data_container.append(chart_data)
        data_container.append(chart_data_2)
    return jsonify(data_container)

@app.route('/actionsByUser', methods=['POST'])
def actionsByUser():
    if request.method == 'POST':
        analyze = Analyze()
        post_data = request.get_json()
        table_data = analyze.get_non_missing_actions_for_user(post_data)
    return jsonify(table_data)

@app.route('/fetchDrillDownDataForForm', methods=['POST'])
def fetchDrillDownDataForForm():
    if request.method == 'POST':
        analyze = Analyze()
        post_data = request.get_json()
        action_data = analyze.fetch_drill_down_data_for_form(post_data)
    return jsonify(action_data)

@app.route('/updateAction', methods=['POST'])
def updateAction():
    if request.method == 'POST':
        db = Connection()
        analyze = Analyze()
        post_data = request.get_json()
        db.updateAction(post_data)
        post_data['ieNumber'] = post_data['userIENumber']
        table_data = analyze.get_non_missing_actions_for_user(post_data)
    return jsonify(table_data)

@app.route('/filterTable', methods=['POST'])
def filterTable():
    if request.method == 'POST':
        db = Connection()
        analyze = Analyze()
        post_data = request.get_json()
        column_list = db.determine_values_in_table_filter(post_data)
        # I don't believe that I need to do a search for when the action number is 
        # used - there should only be one matching action number. I mean when action
        # number is used I could simple search off that...fix???
        if len(column_list) == 3:
            table_data = analyze.filter_table_by_one_column(column_list)
        if len(column_list) == 5:
            table_data = analyze.filter_table_by_two_columns(column_list)
        if len(column_list) == 7:
            table_data = analyze.filter_table_by_three_columns(column_list)
        if len(column_list) == 9:
            table_data = analyze.filter_table_by_four_columns(column_list)
    return jsonify(table_data)


@app.route('/fetchDrillDownDataForGraphs', methods=['POST'])
def fetchDrillDownDataForGraphs():
    if request.method == 'POST':
        analyze = Analyze()
        post_data = request.get_json()
        if len(post_data) == 2:
            table_data = analyze.getDrillDownData(post_data)
        elif post_data['needsIENUMBER']:
            table_data = analyze.getDrillDownDataIENumberSelectionCharts(post_data)
        else: 
            table_data = analyze.getDrillDownDataStackedChart(post_data)
    return jsonify(table_data)

if __name__ == '__main__':
    app.run()