# Create a dictionary with user information
user = {
    "name": "Elias",       # key "name" with value "Elias"
    "age": 24,             # key "age" with value 24
    "city": "Porto Velho"  # key "city" with value "Porto Velho"
}

# Ask the user to input a new city
city = input("Choose a city: ")

# Update the value of the key "city" with the new input
user["city"] = city

# Print the updated dictionary
print(user)  # Output will show the new city chosen by the user