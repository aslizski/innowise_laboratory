"""
Module user_profile have useful func:
    generate_profile() -generation of users life-stage
    user_age() - returns user age
"""


def user_age(birth_year):
    """
       Returns age based on birth year.
    """
    return 2025 - birth_year


def generate_profile(age):
    """
    Define user stage

    arguments:
    age(int) - user age (must be >0)

    returns:
    str - category of user
    """
    if age < 0:
        return "Wrong number"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"


def profile_summary(all_info):
    print("---")
    print("Profile Summary: ")
    # Loop through all profile items and print them
    for key, value in all_info.items():
        # Special handling for hobbies because it's a list
        if key == "Hobbies":
            if value:
                print(f"Favorite Hobbies ({len(value)}): ")
                for hobby in value:
                    print(f"- {hobby}")
            else:
                print("You didn't mention any hobbies.")
            continue

        print(f"{key}: {value}")
    print("---")
