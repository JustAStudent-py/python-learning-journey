# List of users
users = [
    {"name": "ana", "age": 17},
    {"name": "joao", "age": 22},
    {"name": "maria", "age": 19},
    {"name": "pedro", "age": 15}
]

# Function to count and list users under 18
def count_not_adults(users):
    not_adults = []
    count = 0

    # Loop through each user
    for user in users:
        # Check if user is under 18
        if user['age'] < 18:
            count += 1
            not_adults.append(user)

    # Return both count and list
    return count, not_adults


# Call function
print(count_not_adults(users))