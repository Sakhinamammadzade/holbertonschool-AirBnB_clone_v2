-- create db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- set privileges to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- set privileges to user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- apply changes
FLUSH PRIVILEGES;
