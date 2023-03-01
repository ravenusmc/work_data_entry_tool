
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
    
    def get_graph_data_ienumber_by_action(self):
        chart_data = []
        columns = ['Action Type', 'Count']
        chart_data.append(columns)
        action_types = ['101', '500', '702', '792']
        ieNumber = 'ie7046'
        for action_type in action_types:
            rows = []
            query = ("""SELECT COUNT(NOA) FROM actions WHERE Processor_ieNumber = %s""")
            self.cursor.execute(query, (ieNumber,))
            row = self.cursor.fetchone()
            rows.append(action_type)
            rows.append(row[0])
            chart_data.append(rows)
        print(chart_data)



obj = Analyze()
# obj.get_all_actions_by_noa()
# obj.get_recruit_vs_nonrecruit()
obj.get_graph_data_ienumber_by_action()
