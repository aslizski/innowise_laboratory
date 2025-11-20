"""
Module user_profile have useful func:
    generate_profile() -generation of users life-stage
    profile_summary() - returns user formatted summary
"""


def generate_profile(age):
    """
    Define user stage

    arguments:
    age(int) - user age (must be >0)

    returns:
    str - category of user
    """

    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
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
