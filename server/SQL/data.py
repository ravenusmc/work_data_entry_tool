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

    def create_random_data(self):
        creator = Creator()
        count = 0
        while count < 12:
            data_holder = {}
            full_action_number = creator.create_action_number(count)
            data_holder['action_number'] = full_action_number
            print(data_holder)
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
obj.create_random_data()




# {'action_number': 'TST-TST-2023-0002', 'user_id': 1, 'selectedValueRecruitAction': False, 
# 'title': 'New person', 'create_date': '2023-02-01', 'effective_date': '2023-02-02', 
# 'received_by_class': '2023-02-03', 'received_by_staffing': '2023-02-04', 
# 'received_by_processing': '2023-02-05', 'NOA': '101', 'Authority': 'BWA', 'Processor_ieNumber': 'ie7046', 
# 'Date_Receievd': '2023-02-07', 'Returned': False, 'Keyed': True, 'Applied': True}