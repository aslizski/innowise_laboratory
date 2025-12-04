import sqlite3
from functions import run_query, run_many, table_empty, fetch_all
import sql_queries as q

"""
Main script for Student Grades Manager.
Creates database, tables, inserts sample data, and runs queries.
"""

# Connect to database
db = sqlite3.connect('school.db')
cursor = db.cursor()

# Enable foreign key support
run_query(cursor, "PRAGMA foreign_keys = ON;")

"""
Create tables if they don't exist
"""
run_query(cursor, q.CREATE_TABLE_STUDENTS)
run_query(cursor, q.CREATE_TABLE_GRADES)

"""
Insert sample student data if table is empty
"""
students = [
    ('Alice Johnson', 2005), ('Brian Smith', 2004), ('Carla Reyes', 2006),
    ('Daniel Kim', 2005), ('Eva Thompson', 2003), ('Felix Nguyen', 2007),
    ('Grace Patel', 2005), ('Henry Lopez', 2004), ('Isabella Martinez', 2006)
]

if table_empty(cursor, "SELECT COUNT(*) FROM students"):
    run_many(cursor, q.INSERT_STUDENT, students)

"""
Insert sample grades data if table is empty
"""
grades = [
    (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
    (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
    (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
    (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
    (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
    (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
    (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
    (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
    (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92)
]

if table_empty(cursor, "SELECT COUNT(*) FROM grades"):
    run_many(cursor, q.INSERT_GRADE, grades)

# Save changes
db.commit()

"""
Run queries and print results
"""
print("Grades for Alice Johnson:")
print(fetch_all(cursor, q.SELECT_GRADES_ALICE))

print("Average grade per student:")
print(fetch_all(cursor, q.SELECT_AVG_PER_STUDENT))

print("Students born after 2004:")
print(fetch_all(cursor, q.SELECT_STUDENTS_AFTER_2004))

print("Average grade per subject:")
print(fetch_all(cursor, q.SELECT_AVG_PER_SUBJECT))

print("Top 3 students by average grade:")
print(fetch_all(cursor, q.SELECT_TOP_3_STUDENTS))

print("Students with any grade below 80:")
print(fetch_all(cursor, q.SELECT_STUDENTS_BELOW_80))

# Close database
db.close()
