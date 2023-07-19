-- Script that creates a table called id_not_null in the current database
-- in a MySQL server, the id has a default value 1

-- CREATE keyword is used for creating tables in a mysql database
CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1,
name VARCHAR(256) NOT NULL
);
