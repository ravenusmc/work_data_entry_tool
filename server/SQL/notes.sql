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

        <!-- :settings="{ allowHTML: true }" -->

        
SQL reference from previous projects:
https://github.com/ravenusmc/statues/blob/main/server/sql/tables.sql

https://stackoverflow.com/questions/43193721/vue-js-dynamic-dropdown

REFERENCES CONTINUED: 
https://stackoverflow.com/questions/43796423/python-converting-mysql-query-result-to-json
https://www.tutorialspoint.com/explain-the-use-of-count-and-sum-in-mysql-using-python
https://github.com/ravenusmc/dress_reviews/blob/main/client/src/views/Main.vue

Github Drill Down:
https://github.com/ravenusmc/statues/blob/main/client/src/components/Graphs/GraphCard.vue
https://github.com/ravenusmc/statues/blob/main/client/src/components/data/Modal.vue


//['TST-TST-2023-0001', 'Sun, 01 Jan 2023 00:00:00 GMT', 1, 1, 101, 'BWA', 'ie7046', 'Sun, 29 Jan 2023 00:00:00 GMT', 0, 1, __ob__: Observer]
// action_number, date_created, recruit_action, user_id, NOA,
//             Authority, Processor_ieNumber, Date_Receieved, Returned, Keyed
//             Applied