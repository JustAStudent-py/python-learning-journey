# List of users with name and age
users = [
    {"name": "ana", "age": 17},
    {"name": "joao", "age": 22},
    {"name": "maria", "age": 19},
    {"name": "pedro", "age": 15}
]

# Function to extract only the names from users
def only_names(users):
    usernames = []

    # Loop through each user
    for user in users:
        # Add the 'name' value to the list
        usernames.append(user['name'])
    
    # Return list of names
    return usernames


# Call function and print result
print(only_names(users))