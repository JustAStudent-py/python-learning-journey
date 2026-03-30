# Tuple that stores the days of the week
week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Ask the user to choose a number between 1 and 7
user_choice = int(input("Choose a number (1-7): "))

# Check if the number is between 1 and 7
if 1 <= user_choice <= 7:
    
    # Calculate the correct index (because tuples start at index 0)
    index = user_choice - 1
    
    # Print the day that corresponds to the number
    print(week[index])

else:
    # If the number is not between 1 and 7
    print("Choose a valid number.")