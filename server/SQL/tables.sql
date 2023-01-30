
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
  user_id INT NOT NULL,
  recruit_action BOOLEAN, 
  action_number VARCHAR(240) NOT NULL,
  NOA INT NOT NULL,
  Authority VARCHAR(240) NOT NULL,
  Processor_ieNumber VARCHAR(240) NOT NULL, 
  Date_Receievd TIMESTAMP, 
  Returned BOOLEAN,
  Keyed BOOLEAN, 
  Applied BOOLEAN, 
  FOREIGN KEY (user_id) REFERENCES users(user_id)
  PRIMARY KEY(action_id)
);

Show databases;

DESCRIBE users;

DROP TABLE users;

-- Use dresses; 

-- DELETE FROM users WHERE user_id = 2;