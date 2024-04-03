-- create db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- set privileges to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- set privileges to user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- apply changes
FLUSH PRIVILEGES;
