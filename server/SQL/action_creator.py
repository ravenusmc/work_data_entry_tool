import random


class Creator():

    def create_action_number(self, count):
        random_int = random.randint(0,2)
        action_types = ['TST-TST-2023-', 'END-END-2023-', 'LAS-LAS-2023-']
        action_type = action_types[random_int]
        if count < 10:
            ending = '000' + str(count)
        else: 
            ending = '00' + str(count)
        full_action_number = action_type + ending
        return full_action_number
    
    def create_user_id(self):
        


# 'action_number': 'TST-TST-2023-0002',

