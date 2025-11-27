def new_student(students):
    """
    Adds a new student to the list if the name does not already exist.

    Args:
        students (list): List of student dictionaries.
    """
    while True:

        name = input("Enter student name: ").strip().lower().title()
        if not name:
            print("Name cannot be empty.")
            continue
        if any(student["name"] == name for student in students):
            print("This name is already exist")
            continue

        new_person = {"name": name,
                      "grades": []
                      }
        students.append(new_person)
        break


def new_grade(students):
    name = input("Enter student name: ").lower().title()
    if any(student["name"] == name for student in students):
        for student in students:
            if student["name"] == name:
                while True:
                    user_input = input("Enter a grade (or 'done' to finish): ").strip().lower()
                    if user_input == "done":
                        break
                    try:
                        grade = int(user_input)

                    except ValueError:
                        print("Invalid input. Please enter a number")
                        continue

                    if grade > 100 or grade < 0:
                        print("Invalid input. Please enter a number")
                        continue
                    else:
                        student["grades"].append(grade)
    else:
        print("Student is not found")


def show_report(students):
    print("--- Student Grade Analyzer ---")
    students_average = []
    if len(students) == 0:
        print("There is no students")
    else:
        for student in students:
            try:
                average = sum(student["grades"]) / len(student["grades"])
                print(f"{student["name"]}'s average grade is {average:.1f}")
                students_average.append(average)
            except ZeroDivisionError:
                print(f"{student["name"]}'s average grade is N/A")
        print("-----------------------------")
        if students_average:
            print(f"Max Average: {max(students_average):.1f}")
            print(f"Min Average: {min(students_average):.1f}")
            print(f"Overall Average: {sum(students_average) / len(students_average):.1f}")
        else:
            print("No grades to calculate statistics.")


def top_perfomer(students):
    if not students:
        print("There are no students.")
        return

    students_with_grades = [s for s in students if s["grades"]]

    if not students_with_grades:
        print("No student has grades yet. Top student cannot be determined.")
        return

    top_student = max(
        students_with_grades,
        key=lambda student: sum(student["grades"]) / len(student["grades"])
    )

    average = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"The student with the highest average is {top_student["name"]} with a grade of {average:.1f}")
