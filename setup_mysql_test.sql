-- MySQL Script that prepares the server for this project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL on hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT on performance_schema.* TO 'hbnb_test'@'localhost';
