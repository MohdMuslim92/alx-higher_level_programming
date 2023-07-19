-- Script that creates the database hbtn_0d_usa and the
-- table states (in the database hbtn_0d_usa)
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null

-- CREATE keyword is used for creating tables in a mysql database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
name VARCHAR(256) NOT NULL
);
