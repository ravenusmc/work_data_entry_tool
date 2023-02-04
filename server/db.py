# This file will handle the connection to the database

# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime


class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                            password='pass',
                                            host='localhost',
                                            port=3306,
                                            database='work_data_entry_tool')
        self.cursor = self.conn.cursor()

    def encrypt_pass(self, post_data):
        password = post_data['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed

    # This method will insert a new user into the database.
    def insert(self, user, hashed):
        user_created = True
        self._SQL = """insert into users
      (firstName, lastName, email, ieNumber, password)
      values
      (%s, %s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (user.first_name,
                            user.last_name, user.email, user.ieNumber, hashed))
        self.conn.commit()
        return user_created

    # This method will check to ensure that the username is in the database.
    def check(self, ieNumber, password):
        # Setting up a user dictionary
        user = {}
        # encoding the password to utf-8
        password = password.encode('utf-8')
        # Creating the query for the database
        query = ("""SELECT * FROM users WHERE ieNumber = %s""")
        self.cursor.execute(query, (ieNumber,))
        row = self.cursor.fetchone()
        # Here I check to see if the username is in the database.
        if str(row) == 'None':
            login_flag = False
            not_found = True
            password_no_match = False
        # If the user name is in the database I move here to check if the password
        # is valid.
        else:
            hashed = row[5].encode('utf-8')
            if bcrypt.hashpw(password, hashed) == str(hashed, 'UTF-8'):
                user["id"] = row[0]
                user['first_name'] = row[1]
                user['last_name'] = row[2]
                user['email'] = row[3]
                user['ieNumber'] = row[4]
                login_flag = True
                not_found = False
                password_no_match = False
            # This is a final catch all area. Basically if the password does not match
            # the user is not getting in.
            else:
                login_flag = False
                not_found = False
                password_no_match = True
        return login_flag, not_found, password_no_match, user

    def locateAction(self, post_data):
        query = ("""SELECT * FROM actions WHERE action_number = %s""")
        self.cursor.execute(query, (post_data['actionNumber'],))
        row = self.cursor.fetchone()
        if str(row) == 'None':
            return False
        else:
            return True

    def submitAction(self, post_data):
        self._SQL = """insert into actions 
        (user_id, recruit_action, action_number, NOA, Authority, Processor_ieNumber, Date_Receieved, Returned, Keyed, Applied)
        values
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (post_data['user_id'], post_data['recruit_action'], post_data['action_number'], post_data['NOA'], post_data['Authority'],
        post_data['Processor_ieNumber'], post_data['Date_Receieved'], post_data['Returned'], post_data['Keyed'], post_data['Applied']))
        self.conn.commit()
        print('CHECK!!')

