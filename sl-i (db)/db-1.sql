CREATE TABLE Students (
student_id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50),
email VARCHAR(100) UNIQUE,
age INT CHECK (age >= 18),
course_id INT,
CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
CREATE TABLE Courses (
course_id INT PRIMARY KEY AUTO_INCREMENT,
course_name VARCHAR(100) NOT NULL,
credits INT DEFAULT 3
);
CREATE INDEX idx_lastname ON Students(last_name);
CREATE VIEW StudentDetails AS
SELECT s.student_id, s.first_name, s.last_name, c.course_name, c.credits
FROM Students s
JOIN Courses c ON s.course_id = c.course_id;
CREATE TABLE StudentSeq (
id INT PRIMARY KEY AUTO_INCREMENT
);
INSERT INTO Courses (course_name, credits) VALUES ('Database Systems', 4);
INSERT INTO Courses (course_name, credits) VALUES ('Operating Systems', 3);
INSERT INTO Students (first_name, last_name, email, age, course_id)
VALUES ('Nishtha', 'Pardesi', 'nishtha@example.com', 19, 1);
INSERT INTO Students (first_name, last_name, email, age, course_id)
VALUES ('Pratik', 'Paralikar', 'pratik@example.com', 20, 1);
INSERT INTO Students (first_name, last_name, email, age, course_id)
VALUES ('Ananya', 'Chavan', 'ananya@example.com', 19, 2);
UPDATE Students SET email = 'nishtha.patil@example.com' WHERE student_id = 1;
DELETE FROM Students WHERE student_id = 2;
SELECT * FROM Students;
SELECT * FROM StudentDetails;
SELECT first_name, last_name FROM Students WHERE age > 20;
SELECT course_id, COUNT(*) AS total_students
FROM Students
GROUP BY course_id;
SELECT course_name FROM Courses ORDER BY credits DESC LIMIT 1;
SELECT * FROM Students ORDER BY last_name ASC;