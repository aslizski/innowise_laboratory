from user_profile import generate_profile, profile_summary
import datetime

# Ask for user's name
user_name = input("Hello! Please, provide us your full name: ")
birth_year_str = input("Enter your birth date: ")

# convert birth year to int
birth_year = int(birth_year_str)

# Calculate age using datetime.year
current_date = datetime.datetime.now().year
current_age = current_date - birth_year

# Collect hobbies from the user until they type 'stop'
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

# user life stage
life_stage = generate_profile(current_age)

# Create final user profile dictionary
user_profile = {
    "Name": user_name.title(),
    "Age": current_age,
    "Life Stage": life_stage,
    "Hobbies": hobbies
}

# Print formatted summary
profile_summary(user_profile)
