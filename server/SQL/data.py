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
        while count < 12:
            data_holder = {}
            data_holder['action_number'] = creator.create_action_number(support, count)
            data_holder['user_id'] = creator.create_user_id(support)
            data_holder['recruit_action'] = creator.create_recruit_action_boolean(support)
            data_holder['title'] = creator.create_title(support)
            data_holder['create_date'] = creator.create_date(support, 'create_date')
            data_holder['effective_date'] = creator.create_date(support, 'effective_date')
            data_holder['received_by_class'] = creator.create_date(support, 'received_by_class')
            data_holder['received_by_staffing'] = creator.create_date(support, 'received_by_staffing')            
            data_holder['received_by_processing'] = creator.create_date(support, 'received_by_processing')
            data_holder['NOA'] = creator.create_NOA(data_holder['title'])
            data_holder['Authority'] = creator.create_authority(data_holder['NOA'])
            data_holder['Processor_ieNumber'] = creator.create_ieNumber(support)
            data_holder['Date_Receievd'] = data_holder['received_by_processing']
            data_holder['Returned'] = creator.true_false_selector(support)
            data_holder['Keyed'] = creator.true_false_selector(support)
            if data_holder['Keyed'] == False:
                data_holder['Applied'] = False 
            else:
                data_holder['Applied'] = creator.true_false_selector(support)
            count+=1
    


    # def submitMissingActionToDatabase(self, post_data):
    #     self._SQL = """insert into missing_actions
    #     (action_number, user_id, recruit_action, title, create_date, effective_date,
    #     received_by_class, received_by_staffing, received_by_processing, NOA, Authority, 
    #     Processor_ieNumber, Date_Receievd, Returned, Keyed, Applied)
    #     values
    #     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #     self.cursor.execute(self._SQL, (post_data['action_number'], post_data['user_id'], post_data['selectedValueRecruitAction'],
    #                                     post_data['title'], post_data['create_date'], post_data[
    #                                         'effective_date'], post_data['received_by_class'],
    #                                     post_data['received_by_staffing'], post_data[
    #                                         'received_by_processing'], post_data['NOA'], post_data['Authority'],
    #                                     post_data['Processor_ieNumber'], post_data['Date_Receievd'], post_data['Returned'], post_data['Keyed'],
    #                                     post_data['Applied']))
    #     self.conn.commit()


obj = Connection()
obj.create_random_data_missing_actions()


# {'action_number': 'TST-TST-2023-0002', 'user_id': 1, 'selectedValueRecruitAction': False, 
# 'title': 'New person', 'create_date': '2023-02-01', 'effective_date': '2023-02-02', 
# 'received_by_class': '2023-02-03', 'received_by_staffing': '2023-02-04', 
# 'received_by_processing': '2023-02-05', 'NOA': '101', 'Authority': 'BWA', 'Processor_ieNumber': 'ie7046', 
# 'Date_Receievd': '2023-02-07', 'Returned': False, 'Keyed': True, 'Applied': True}