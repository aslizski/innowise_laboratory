"""
SQL queries for Student Grades Manager.
This file contains all the SQL statements used in the project:
- Table creation
- Data insertion
- Data selection queries
"""

"""Create the 'students' table.
Columns:
- id: unique student identifier, INTEGER PRIMARY KEY
- full_name: student full name, TEXT
- birth_year: year of birth, INTEGER"""
CREATE_TABLE_STUDENTS = """

CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    birth_year INTEGER
)
"""
"""Create the 'grades' table.
Columns:
- id: unique grade identifier, INTEGER PRIMARY KEY
- student_id: foreign key referencing students.id
- subject: name of the subject, TEXT
- grade: numeric grade (1-100), INTEGER"""
CREATE_TABLE_GRADES = """
CREATE TABLE IF NOT EXISTS grades(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
"""

INSERT_STUDENT = """
INSERT INTO students (full_name, birth_year) VALUES (?, ?)
"""

INSERT_GRADE = """
INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)
"""

SELECT_ALL_STUDENTS = """
SELECT * FROM students
"""

SELECT_ALL_GRADES = """
SELECT * FROM grades
"""

#  Find all grades for Alice Johnson
SELECT_GRADES_ALICE = """
SELECT grades.subject, grades.grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE students.full_name = 'Alice Johnson'
"""

# Average grade per student
SELECT_AVG_PER_STUDENT = """
SELECT students.full_name, ROUND(AVG(grades.grade), 2) AS average_grade
FROM students
JOIN grades ON grades.student_id = students.id
GROUP BY students.id
"""

#  Students born after 2004
SELECT_STUDENTS_AFTER_2004 = """
SELECT *
FROM students
WHERE students.birth_year > 2004
"""

#  Average grade per subject
SELECT_AVG_PER_SUBJECT = """
SELECT grades.subject, ROUND(AVG(grades.grade), 2) AS average_grade
FROM grades
GROUP BY grades.subject
"""

#  Top 3 students with highest average grades
SELECT_TOP_3_STUDENTS = """
SELECT students.full_name, ROUND(AVG(grades.grade), 2) AS average_grade
FROM students
JOIN grades ON grades.student_id = students.id
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 3
"""

# Students with any grade below 80
SELECT_STUDENTS_BELOW_80 = """
SELECT DISTINCT students.full_name, grades.subject, grades.grade
FROM students
JOIN grades ON grades.student_id = students.id
WHERE grades.grade < 80
"""
