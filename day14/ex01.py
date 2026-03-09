# Create a dictionary with fruit names as keys and their prices as values
fruits = {
    "banana": 2,  # key "banana" with value 2
    "orange": 4,  # key "orange" with value 4
    "lemon": 3,   # key "lemon" with value 3
    "apple": 2    # key "apple" with value 2
}

# Loop through the dictionary and get both key and value
for key, value in fruits.items():
    print(f"Product: {key} - price: ${value}")  # Output format: Product: banana - price: 2