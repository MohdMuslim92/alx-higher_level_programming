-- Script that creates a table called force_name in the current database in a MySQL server

-- CREATE keyword is used for creating tables in a mysql database
CREATE TABLE IF NOT EXISTS force_name(
id INT,
name VARCHAR(256) NOT NULL
);
