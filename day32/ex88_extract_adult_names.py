# List of users
users = [
    {"name": "ana", "age": 17},
    {"name": "joao", "age": 22},
    {"name": "maria", "age": 19},
    {"name": "pedro", "age": 15}
]

# Function to return names of adult users
def adults_names(users):
    names = []

    # Loop through each user
    for user in users:
        # Check if user is an adult
        if user['age'] >= 18:
            # Add only the name
            names.append(user['name'])

    return names


# Call function
print(adults_names(users))