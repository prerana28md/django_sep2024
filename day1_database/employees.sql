DROP DATABASE IF EXISTS my_database;
CREATE DATABASE my_database;
USE my_database;

CREATE TABLE employees (
 id INT PRIMARY KEY,
 name VARCHAR(50) NOT NULL,
 dept_id INT,
 job_title VARCHAR(50),
 salary DECIMAL(10, 2)
);
INSERT INTO employees (id, name, dept_id, job_title, salary) 
VALUES (1, 'Chris', 3, 'Analyst', 50000.00),
(2,'Raju',45,'Developer',34500.9);


