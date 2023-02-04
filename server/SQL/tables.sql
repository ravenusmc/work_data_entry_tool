
CREATE DATABASE work_data_entry_tool;

use work_data_entry_tool;

--Table for the users. 
CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  firstName VARCHAR(240) NOT NULL,
  lastName VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  ieNumber VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);

--Do I need two tables? Recruit and non Recruit?? - I think I can do this with one table
--but create a boolean for recruit action => 0 it's not and 1 it is. 
CREATE TABLE actions 
(
  action_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  action_number VARCHAR(240) NOT NULL,
  date_created TIMESTAMP NOT NULL, 
  recruit_action BOOLEAN NOT NULL,
  user_id INT,
  NOA INT,
  Authority VARCHAR(240),
  Processor_ieNumber VARCHAR(240), 
  Date_Receieved TIMESTAMP, 
  Returned BOOLEAN,
  Keyed BOOLEAN, 
  Applied BOOLEAN, 
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

--Table for missing actions 
CREATE TABLE missing_actions 
(
  action_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  recruit_action BOOLEAN NOT NULL, 
  action_number VARCHAR(240) NOT NULL,
  title VARCHAR(240) NOT NULL,
  create_date TIMESTAMP NOT NULL, 
  effective_date TIMESTAMP NOT NULL, 
  received_by_class TIMESTAMP NOT NULL, 
  received_by_staffing TIMESTAMP NOT NULL, 
  received_by_processing TIMESTAMP NOT NULL, 
  NOA INT NOT NULL,
  Authority VARCHAR(240) NOT NULL,
  Processor_ieNumber VARCHAR(240) NOT NULL, 
  Date_Receievd TIMESTAMP NOT NULL, 
  Returned BOOLEAN,
  Keyed BOOLEAN, 
  Applied BOOLEAN, 
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

Show databases;

DESCRIBE users;

DROP TABLE users;


-- DELETE FROM users WHERE user_id = 2;

-- Inserting data 
INSERT INTO actions
(action_id, action_number, date_created, recruit_action)
VALUES (1, 'TST-TST-2023-0001', '2023-01-01', 1);
-- INSERT INTO actions
-- VALUES (1, 1, True, 'TST-TST-2023-0001', 101, 'BWA', 'ie7046', '2023-01-01', False, True, True);

DELETE FROM actions WHERE action_id = 1;