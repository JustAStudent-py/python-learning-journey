# List of users with name and age
users = [
    {"name": "ana", "age": 17},
    {"name": "joao", "age": 22},
    {"name": "maria", "age": 19},
    {"name": "pedro", "age": 15}
]


# Function to filter only adult users (age >= 18)
def only_adults(users):
    adults = []

    # Loop through each user in the list
    for user in users:
        # Check if the user is an adult
        if user['age'] >= 18:
            adults.append(user)
        else:
            # Inform that the user is not an adult
            print(f"{user['name']} is not an adult.")

    # Return list of adult users
    return adults


# Call function and print result
print(only_adults(users))