
-- 1. Write a SQL query for creating a new table with three columns: student_id, name and age.
-- Set the student_id column to be the primary key.

CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	student_name TEXT,
	student_age INTEGER
);

-- 2. Write a SQL query for inserting a student into the 
-- table defined above. The student’s name is John Doe, age 26, with student ID 736. 

INSERT INTO students (student_id, student_name, student_age)
VALUES (736, 'John Doe', 26);

-- 3. Oops! That’s not right. John Doe is 27, not 26. Write a SQL query to update John Doe’s entry.

UPDATE students
SET student_age = 27
WHERE student_id = 736;

-- 4. John has graduated. Write a SQL query to delete John’s row.

DELETE FROM students
WHERE student_id = 736;

-- 5. Write a SQL query to delete the table.

DROP TABLE students;