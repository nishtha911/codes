-- Table Creation
--------------------------------------------------------------------------------

-- CREATE TABLE Departments
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL
);

-- CREATE TABLE Employees
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2),
    dept_id INT,
    manager_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id),
    -- Self-referencing FK for manager
    FOREIGN KEY (manager_id) REFERENCES Employees(emp_id)
);

-- Data Insertion
--------------------------------------------------------------------------------

-- INSERT INTO Departments
INSERT INTO Departments (dept_name) VALUES ('HR'), ('IT'), ('Finance');

-- INSERT INTO Employees
INSERT INTO Employees (emp_name, salary, dept_id, manager_id) VALUES
('Nishtha', 50000, 1, NULL),
('Ananya', 60000, 2, 1),
('Pratik', 55000, 2, 1),
('Soham', 45000, 3, 2),
('Disha', 70000, 2, NULL); -- Disha has no manager in this data, like Nishtha

-- View Creation
--------------------------------------------------------------------------------

-- #1 CREATE VIEW EmpDetails
CREATE VIEW EmpDetails AS
SELECT e.emp_id, e.emp_name, e.salary, d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;

-- SQL Queries
--------------------------------------------------------------------------------

-- #2 INNER JOIN: Select all columns for employees and their department details
SELECT * FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id;

-- #3 LEFT JOIN: Select employee name and department name (includes employees even if dept_id is NULL)
SELECT e.emp_name, d.dept_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id;

-- #4 RIGHT JOIN: Select employee name and department name (includes departments even if they have no employees)
-- Note: MySQL interprets a standard RIGHT JOIN similarly to an OUTER JOIN when used with a LEFT JOIN equivalent, 
-- but its primary role here is to ensure all Departments are included.
SELECT e.emp_name, d.dept_name
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id;

-- #5 FULL JOIN: Emulating a FULL OUTER JOIN (combines LEFT and RIGHT joins).
-- MySQL does not support the standard FULL JOIN syntax, so we use UNION.
SELECT e.emp_name, d.dept_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
UNION
SELECT e.emp_name, d.dept_name
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL; -- Only shows unmatched records from the right side once

-- #6 Subquery: Select employees with salary greater than the average salary
SELECT emp_name, salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);

-- #7 Subquery: Select employees who belong to the 'IT' department
SELECT emp_name
FROM Employees
WHERE dept_id = (
    SELECT dept_id
    FROM Departments
    WHERE dept_name = 'IT'
);

-- #8 Select from the created VIEW
SELECT * FROM EmpDetails;

-- #9 GROUP BY and HAVING: Find departments with more than 1 employee
SELECT d.dept_name, COUNT(*) AS total_employees
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(*) > 1;

-- #10 EXISTS/NOT EXISTS: Find employees who are *not* managers (i.e., their emp_id is not in the manager_id column of *any* other employee)
-- This query, based on the original logic, is typically used to find employees who do *not* report to anyone (manager_id IS NULL), 
-- or to find employees who are *not* themselves managers (NOT EXISTS in subquery).
-- Assuming the intent is to find employees who are *not* listed as a manager for any other employee:
SELECT emp_name
FROM Employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM Employees m
    WHERE e.emp_id = m.manager_id
);