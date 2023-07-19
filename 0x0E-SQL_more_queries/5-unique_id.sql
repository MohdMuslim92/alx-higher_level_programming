-- Script that creates a table called id_unique_id in the current database
-- in a MySQL server, the id has a default value 1 and it's a unique

-- CREATE keyword is used for creating tables in a mysql database
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256) NOT NULL
);
