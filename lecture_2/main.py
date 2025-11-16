from user_profile import generate_profile, user_age, profile_summary

# Ask for user's name
user_name = input("Hello! Please, provide us your full name: ")
birth_year_str = input("Enter your birth date: ")


# convert birth year to int
birth_year = int(birth_year_str)

# Calculate age using function from the module
current_age = user_age(birth_year)

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
    "Stage": life_stage,
    "Hobbies": hobbies
}

# Print formatted summary
profile_summary(user_profile)
