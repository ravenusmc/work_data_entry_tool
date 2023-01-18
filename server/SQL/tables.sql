
CREATE DATABASE work_data_entry_tool;

use work_data_entry_tool;;

CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  firstName VARCHAR(240) NOT NULL,
  lastName VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  idNumber VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);

Show databases;

-- Use dresses; 

-- DELETE FROM users WHERE user_id = 2;