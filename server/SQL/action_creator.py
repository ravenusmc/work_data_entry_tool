# Importing files that I created for the project
from support import *


class Creator():

    def create_action_number(self, obj, count):
        random_int = obj.random_number_generator(0,2)
        action_types = ['TST-TST-2023-', 'END-END-2023-', 'LAS-LAS-2023-']
        action_type = action_types[random_int]
        if count < 10:
            ending = '000' + str(count)
        else: 
            ending = '00' + str(count)
        full_action_number = action_type + ending
        return full_action_number
    
    def create_user_id(self):
        support = Support()
        user_id = support.random_number_generator(0,4)
        return user_id
    
    def create_recruit_action_boolean(self):
        support = Support()
        rand_int = support.random_number_generator(0,1)
        values = [True, False]
        selected_value = values[rand_int]
        return selected_value
    
    def create_title(self, obj):
        rand_int = obj.random_number_generator(0,3)
        titles = ['Promotion', 'Chg in Duty Station', 'Accession', 'Conversion']
        title = titles[rand_int]
        return title 

        


# 'action_number': 'TST-TST-2023-0002',

