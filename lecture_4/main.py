from functions import execute_script, run_query

"""
Main script that creates the database using school.sql
and then demonstrates running example SELECT queries.
"""

DB_PATH = "school.db"
SQL_SCRIPT = "school.sql"

# Create database and insert data
execute_script(DB_PATH, SQL_SCRIPT)

# get all grades for Alice Johnson
result_1 = run_query(DB_PATH, "SELECT * FROM grades WHERE student_id = 1;")
print("Grades for Alice Johnson:", result_1)

# average grade per student
result_2 = run_query(DB_PATH, """
SELECT students.full_name, ROUND(AVG(grades.grade),2)
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id;
""")
print("Average grade per student:", result_2)

# Example: students born after 2004
result_3 = run_query(DB_PATH, "SELECT * FROM students WHERE birth_year > 2004;")
print("Students born after 2004:", result_3)
