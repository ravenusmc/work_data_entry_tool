
# This file will deal with a lot of the data analysis for this project.

# importing supporting libraries
import numpy as np
import pandas as pd
from datetime import datetime
import mysql.connector
import json

# importing files I built.
# from db import *


class Analyze():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                            password='pass',
                                            host='localhost',
                                            port=3306,
                                            database='work_data_entry_tool')
        self.cursor = self.conn.cursor()

    def get_all_actions_by_noa(self):
        chart_data = []
        columns = ['Action Type', 'Count']
        chart_data.append(columns)
        action_types = ['101', '500', '702', '792']
        for action_type in action_types:
            rows = []
            query = ("""SELECT COUNT(NOA) FROM actions WHERE NOA = %s""")
            self.cursor.execute(query, (action_type,))
            row = self.cursor.fetchone()
            rows.append(action_type)
            rows.append(row[0])
            chart_data.append(rows)
        print(chart_data)

    def get_recruit_vs_nonrecruit(self):
        chart_data = []
        columns = ['Recruit Type', 'Count']
        chart_data.append(columns)
        recruit_types = [True, False]
        for recruit_type in recruit_types:
            rows = []
            query = (
                """SELECT COUNT(recruit_action) FROM actions WHERE recruit_action = %s""")
            self.cursor.execute(query, (recruit_type,))
            row = self.cursor.fetchone()
            rows.append(recruit_type)
            rows.append(row[0])
            chart_data.append(rows)
        print(chart_data)

    def get_graph_data_ienumber_by_action(self, post_data):
        chart_data = []
        columns = ['Action Type', 'Count']
        chart_data.append(columns)
        action_types = ['101', '500', '702', '792']
        for action_type in action_types:
            rows = []
            query = ("""SELECT COUNT(NOA) FROM actions WHERE Processor_ieNumber = %s AND
            NOA = %s""")
            self.cursor.execute(query, (post_data['ieNumber'], action_type))
            row = self.cursor.fetchone()
            rows.append(action_type)
            rows.append(row[0])
            chart_data.append(rows)
        return chart_data

    def get_graph_data_by_legal_authority(self):
        chart_data = []
        columns = ['Legal Authority', 'Count']
        chart_data.append(columns)
        legal_authorities = ['MOW', 'CHG', 'ACC', 'CON']
        for legal_athority in legal_authorities:
            rows = []
            query = (
                """SELECT COUNT(Authority) FROM actions WHERE Authority = %s""")
            self.cursor.execute(query, (legal_athority,))
            row = self.cursor.fetchone()
            rows.append(legal_athority)
            rows.append(row[0])
            chart_data.append(rows)
        print(chart_data)

    def get_graph_data_by_recruit_actions(self, post_data):
        chart_data = []
        columns = ['Recruit Action', 'Count']
        chart_data.append(columns)
        boolean_list = [True, False]
        for item in boolean_list:
            rows = []
            query = (
                """SELECT COUNT(recruit_action) FROM actions WHERE recruit_action = %s AND
                Processor_ieNumber = %s""")
            self.cursor.execute(query, (item, post_data['ieNumber']))
            row = self.cursor.fetchone()
            rows.append(str(item))
            rows.append(row[0])
            chart_data.append(rows)
        return chart_data

    def get_graph_data_action_all_users(self):
        chart_data = []
        columns = ['Recruit Action', 'Count']
        chart_data.append(columns)
        action_types = ['101', '500', '702', '792']
        ieNumbers = ['ie7046', 'ie7001',  'ie7002', 'ie7003']
        for action_type in action_types:
            rows = []
            rows.append(action_type)
            for ieNumber in ieNumbers:
                query = ("""SELECT COUNT(NOA) FROM actions WHERE Processor_ieNumber = %s AND
                NOA = %s""")
                self.cursor.execute(query, (ieNumber, action_type))
                row = self.cursor.fetchone()
                rows.append(row[0])
            chart_data.append(rows)
        print(chart_data)

    def get_non_missing_actions_for_user(self, post_data):
        obj = Analyze()
        table_data = []
        columns = ['Action Number', 'Date Created', 'Recruit action', 'NOA',
                   'Authority', 'Processor IENumber', 'Date Received', 'Returned', 
                   'Keyed', 'Applied']
        table_data.append(columns)
        query = ("""SELECT action_number, date_created, recruit_action, NOA, Authority, 
        Processor_ieNumber, Date_Receieved, Returned, Keyed, Applied
        FROM actions WHERE Processor_ieNumber = %s""")
        self.cursor.execute(query, (post_data['ieNumber'],))
        data = self.cursor.fetchall()
        obj.build_table(data, table_data)
        return table_data
    
    def build_table(self, data, table_data):
        count = 0
        print(data[0][1])
        while count < len(data):
            rows = []
            action_number = data[count][0]
            date_created = data[count][1]
            recruit_action = data[count][2]
            NOA = data[count][3]
            Authority = data[count][4]
            Processor_ieNumber = data[count][5]
            Date_Receieved = data[count][6]
            if data[count][7] == 0:
                Returned = 'False'
            elif data[count][7] == 1:
                Returned = 'True'
            if data[count][8] == 0:
                Keyed = 'False'
            elif data[count][8] == 1:
                Keyed = 'True'
            if data[count][9] == 0:
                Applied = 'False'
            elif data[count][9] == 1:
                Applied = 'True'
            rows.append(action_number)
            rows.append(date_created)
            rows.append(recruit_action)
            rows.append(NOA)
            rows.append(Authority)
            rows.append(Processor_ieNumber)
            rows.append(Date_Receieved)
            rows.append(Returned)
            rows.append(Keyed)
            rows.append(Applied)
            table_data.append(rows)
            count += 1
        return table_data


# obj = Analyze()
# obj.get_all_actions_by_noa()
# obj.get_recruit_vs_nonrecruit()
# obj.get_graph_data_ienumber_by_action()
# obj.get_graph_data_by_legal_authority()
# obj.get_graph_data_by_recruit_actions()
# obj.get_graph_data_action_all_users()


