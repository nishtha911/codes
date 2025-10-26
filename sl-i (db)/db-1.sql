CREATE TABLE Departments (
dept_id INT PRIMARY KEY AUTO_INCREMENT,
dept_name VARCHAR(100) NOT NULL
);
CREATE TABLE Employees (
emp_id INT PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(100) NOT NULL,
salary DECIMAL(10,2),
dept_id INT,
manager_id INT,
FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);
INSERT INTO Departments (dept_name) VALUES ('HR'), ('IT'), ('Finance');
INSERT INTO Employees (emp_name, salary, dept_id, manager_id) VALUES
('Nishtha', 50000, 1, NULL),
('Ananya', 60000, 2, 1),
('Pratik', 55000, 2, 1),
('Soham', 45000, 3, 2),
('Disha', 70000, 2, NULL);
--1
CREATE VIEW EmpDetails AS
SELECT e.emp_id, e.emp_name, e.salary, d.dept_nameFROM Employees eJOIN Departments d ON e.dept_id = d.dept_id;
--2
SELECT * FROM Employees e INNER JOIN Departments d ON e.dept_id = d.dept_id;
--3
SELECT e.emp_name, d.dept_name FROM Employees e LEFT JOIN Departments d ON e.dept_id = d.dept_id;
--4
SELECT e.emp_name, d.dept_name FROM Employees e RIGHT JOIN Departments d ON e.dept_id = d.dept_id;
--5
SELECT e.emp_name, d.dept_name FROM Employees e FULL JOIN Departments d ON e.dept_id = d.dept_id;
--6
SELECT emp_name, salary FROM Employees WHERE salary > (SELECT AVG(salary) FROM Employees);
--7
SELECT emp_name FROM Employees WHERE dept_id = (SELECT dept_id FROM Departments WHERE dept_name = 'IT');
--8
SELECT * FROM EmpDetails;
--9
SELECT dept_id, COUNT(*) AS total_employees FROM Employees GROUP BY dept_id HAVING COUNT(*) > 1;
--10
SELECT emp_name FROM Employees e WHERE NOT EXISTS (SELECT 1 FROM Employees m WHERE e.manager_id = m.emp_id);