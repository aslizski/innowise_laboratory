"""
Module user_profile have useful func:
    generate_profile() -generation of users life-stage
    user_age() - returns user age
"""
def user_age(date):
    """
       Returns age based on birth year.
    """
    return 2025 - date

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
    if age <= 12:
        return "Child"
    if age <= 19:
        return "Teenager"
    return "Adult"

def profile_summary(all_info):
    print("---")
    print("Profile Summary: ")
    # Loop through all profile items and print them
    for keys, value in all_info.items():
        # Special handling for hobbies because it's a list
        if keys == "Hobbies":
            if len(value) > 0:
                print(f"Favorite Hobbies ({len(value)}): ")
                for hobby in value:
                    print(f"- {hobby}")
                continue
            else:
                print("You didn't mention any hobbies.")
                continue

        print(f"{keys}: {value}")
    print("---")