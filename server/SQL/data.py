# This file will create blank data for the data base.

# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime

# Importing files that I created for the project
# from data import *
from action_creator import *


class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                            password='pass',
                                            host='localhost',
                                            port=3306,
                                            database='work_data_entry_tool')
        self.cursor = self.conn.cursor()

    def create_random_data_missing_actions(self):
        support = Support()
        creator = Creator()
        count = 0
        while count < 999:
            data_holder = {}
            data_holder['action_number'] = creator.create_action_number(
                support, count)
            data_holder['user_id'] = creator.create_user_id(support)
            data_holder['recruit_action'] = creator.create_recruit_action_boolean(
                support)
            data_holder['title'] = creator.create_title(support)
            data_holder['create_date'] = creator.create_date(
                support, 'create_date')
            data_holder['effective_date'] = creator.create_date(
                support, 'effective_date')
            data_holder['received_by_class'] = creator.create_date(
                support, 'received_by_class')
            data_holder['received_by_staffing'] = creator.create_date(
                support, 'received_by_staffing')
            data_holder['received_by_processing'] = creator.create_date(
                support, 'received_by_processing')
            data_holder['NOA'] = creator.create_NOA(data_holder['title'])
            data_holder['Authority'] = creator.create_authority(
                data_holder['NOA'])
            data_holder['Processor_ieNumber'] = creator.create_ieNumber(
                data_holder['user_id'])
            data_holder['Date_Receievd'] = data_holder['received_by_processing']
            data_holder['Returned'] = creator.true_false_selector(support)
            data_holder['Keyed'] = creator.true_false_selector(support)
            if data_holder['Keyed'] == False:
                data_holder['Applied'] = False
            else:
                data_holder['Applied'] = creator.true_false_selector(support)
            # obj.submitMissingActionToDatabase(data_holder)
            count += 1

    def submitMissingActionToDatabase(self, data_holder):
        self._SQL = """insert into missing_actions
        (action_number, user_id, recruit_action, title, create_date, effective_date,
        received_by_class, received_by_staffing, received_by_processing, NOA, Authority, 
        Processor_ieNumber, Date_Receievd, Returned, Keyed, Applied)
        values
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (data_holder['action_number'], data_holder['user_id'], data_holder['recruit_action'],
                                        data_holder['title'], data_holder['create_date'], data_holder['effective_date'],
                                        data_holder['received_by_class'], data_holder['received_by_staffing'],
                                        data_holder['received_by_processing'], data_holder['NOA'], data_holder['Authority'],
                                        data_holder['Processor_ieNumber'], data_holder[
                                            'Date_Receievd'], data_holder['Returned'], data_holder['Keyed'],
                                        data_holder['Applied']))
        self.conn.commit()

    def create_random_data_for_actions(self):
        support = Support()
        creator = Creator()
        count = 0
        while count < 999:
            data_holder = {}
            data_holder['action_number'] = creator.create_action_number_not_missing(
                support, count)
            data_holder['date_created'] = creator.create_date(
                support, 'create_date')
            data_holder['recruit_action'] = creator.create_recruit_action_boolean(
                support)
            data_holder['user_id'] = creator.create_user_id(support)
            title = creator.create_title(support)
            data_holder['NOA'] = creator.create_NOA(title)
            data_holder['Authority'] = creator.create_authority(
                data_holder['NOA'])
            data_holder['Processor_ieNumber'] = creator.create_ieNumber(
                data_holder['user_id'])
            data_holder['Date_Receieved'] = creator.create_date(
                support, 'received_by_processing')
            data_holder['Returned'] = creator.true_false_selector(support)
            data_holder['Keyed'] = creator.true_false_selector(support)
            if data_holder['Keyed'] == False:
                data_holder['Applied'] = False
            else:
                data_holder['Applied'] = creator.true_false_selector(support)
            obj.submitActionToDatabase(data_holder)
            count += 1
        print('DONE')

    def submitActionToDatabase(self, data_holder):
        self._SQL = """insert into actions
        (action_number, date_created, recruit_action, user_id, NOA, Authority, Processor_ieNumber,
        Date_Receieved, Returned, Keyed, Applied)
        values
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (data_holder['action_number'], data_holder['date_created'], data_holder['recruit_action'],
                                        data_holder['user_id'], data_holder['NOA'], data_holder['Authority'],
                                        data_holder['Processor_ieNumber'], data_holder['Date_Receieved'],
                                        data_holder['Returned'], data_holder['Keyed'], data_holder['Applied']))
        self.conn.commit()

obj = Connection()
# obj.create_random_data_missing_actions()
obj.create_random_data_for_actions()
