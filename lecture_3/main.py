import student_menu
from storage import load_students, save_students

students = load_students()

while True:
    print("""--- Student Grade Analyzer ---
    1. Add a new student 
    2. Add grades for a student
    3. Generate a full report
    4. Find the top student
    5. Exit program""")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input. Please enter a number")
        continue

    if choice == 5:
        save_students(students)
        print("Exiting program.")
        break
    elif choice == 1:
        student_menu.new_student(students)
        save_students(students)
    elif choice == 2:
        student_menu.new_grade(students)
        save_students(students)
    elif choice == 3:
        student_menu.show_report(students)
        save_students(students)
    elif choice == 4:
        student_menu.top_perfomer(students)
        save_students(students)
    else:
        print("Invalid choice!")
