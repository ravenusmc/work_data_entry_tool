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
    
    def create_user_id(self, obj):
        user_id = obj.random_number_generator(0,4)
        return user_id
    
    def create_recruit_action_boolean(self, obj):
        rand_int = obj.random_number_generator(0,1)
        values = [True, False]
        selected_value = values[rand_int]
        return selected_value
    
    def create_title(self, obj):
        rand_int = obj.random_number_generator(0,3)
        titles = ['Promotion', 'Chg in Duty Station', 'Accession', 'Conversion']
        title = titles[rand_int]
        return title 
    
    def create_date(self, obj, date_type):
        year = '2023-'
        rand_month_selector = obj.random_number_generator(0,1)
        # months = ['01-', '02-']
        month = '01-'
        if date_type == 'create_date':
            random_day = obj.random_number_generator(1,5)
        elif date_type == 'effective_date':
            random_day = obj.random_number_generator(25,30)
        elif date_type == 'received_by_class':
            random_day = obj.random_number_generator(6,10)
        elif date_type == 'received_by_staffing':
            random_day = obj.random_number_generator(11,15)
        elif date_type == 'received_by_processing':
            random_day = obj.random_number_generator(16,20)
        date = year + month + str(random_day)
        return date
    
    def create_NOA(self, title):
        if title == 'Promotion':
            return 702
        elif title == 'Chg in Duty Station':
            return 792
        elif title == 'Accession':
            return 101
        elif title == 'Conversion':
            return 500
    
    def create_authority(self, NOA):
        if NOA == 702:
            return 'MOW'
        elif NOA == 792:
            return 'CHG'
        elif NOA == 101:
            return 'ACC'
        elif NOA == 500:
            return 'CON'
    
    def create_ieNumber(self, obj):
        rand_ieNumber_selector = obj.random_number_generator(0,3)
        ieNumbers = ['ie7046', 'ie7000',  'ie7001', 'ie7002']
        return  ieNumbers[rand_ieNumber_selector]
    
    def true_false_selector(self, obj):
        rand_number = obj.random_number_generator(0,1)
        boolean_list = [True, False]
        return boolean_list[rand_number]




# 'action_number': 'TST-TST-2023-0002',

