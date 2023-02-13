--How to update:
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;

--So I'd need to do this: 
UPDATE discussions
SET votes = 
WHERE discussion_id = ;

def update_username_and_email(self, post_data):
        self._SQL = """UPDATE users SET username = %s, email = %s
        where user_id = %s"""
        self.cursor.execute(self._SQL, (post_data['username'], post_data['email'], post_data['id']))
        self.conn.commit()


        --     def update_number_of_votes_on_discussion(self, post_data):
        -- self._SQL = """UPDATE discussions 
        -- SET votes =  %s
        -- where discussion_id = %s"""
        -- self.cursor.execute(
        --     self._SQL, (post_data['numberOfVotesCalculated'], post_data['discussionID']))
        -- self.conn.commit()

SQL reference from previous projects:
https://github.com/ravenusmc/statues/blob/main/server/sql/tables.sql

https://stackoverflow.com/questions/43193721/vue-js-dynamic-dropdown

Applied: true
Authority: "BWA"
Date_Receievd: "2023-02-07"
Keyed: true
NOA: "101"
Processor_ieNumber: 
"ie7046"
Returned
: 
false
action_number
: 
"TST-TST-2023-0002"
create_date
: 
"2023-02-01"
effective_date
: 
"2023-02-02"
received_by_class
: 
"2023-02-03"
received_by_processing
: 
"2023-02-05"
received_by_staffing
: 
"2023-02-04"
selectedValueRecruitAction
: 
false
title
: 
"New person"
user_id
: 
1

