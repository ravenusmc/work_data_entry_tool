    
		# obj.get_graph_data_ienumber_by_action_stacked()
		
		
		# def get_graph_data_ienumber_by_action_stacked(self):
    #     chart_data = []
    #     columns = ['Action Type', 'Count']
    #     chart_data.append(columns)
    #     count = 0
    #     ieNumbers = ['ie7046', 'ie7001', 'ie7002', 'ie7003']
    #     action_types = ['101', '500', '702', '792']
    #     for action_type in action_types:
    #         rows = []
    #         query = ("""SELECT COUNT(NOA) FROM actions WHERE Processor_ieNumber = %s AND
    #         NOA = %s""")
    #         self.cursor.execute(query, (ieNumbers[count], action_type))
    #         row = self.cursor.fetchone()
    #         rows.append(action_type)
    #         rows.append(row[0])
    #         chart_data.append(rows)
    #         count += 1
    #     print(chart_data)