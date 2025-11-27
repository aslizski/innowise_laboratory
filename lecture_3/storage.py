import json


def save_students(students, filename="students.json"):
    """
    Saves the students list to a JSON file.

    Args:
        students (list): List of student dictionaries.
        filename (str): File path to save the data.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)


def load_students(filename="students.json"):
    """
    Loads the students list from a JSON file. Returns an empty list if file not found.

    Args:
        filename (str): File path to load the data from.

    Returns:
        list: List of student dictionaries.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
