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
CREATE VIEW EmpDetails AS
SELECT e.emp_id, e.emp_name, e.salary, d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;
SELECT * FROM Employees e INNER JOIN Departments d ON e.dept_id = d.dept_id;