import random

# Counter to track how many attempts the user makes
attempts = 0

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Display game introduction
print("\n=== Number Guessing Game ===")
print("I have selected a number between 1 and 100.")
print("Try to guess it!\n")

while True:
    # Ask the user to guess the number
    user_number = int(input("Enter your guess: "))
    
    # Increase the attempt counter
    attempts += 1

    # Check if the guess is higher than the secret number
    if user_number > secret_number:
        print("Too high! Try a smaller number.\n")

    # Check if the guess is lower than the secret number
    elif user_number < secret_number:
        print("Too low! Try a bigger number.\n")

    # If the guess is correct
    else:
        print("\nCorrect! 🎉")
        print(f"You guessed the number in {attempts} attempts.")
        print("Game over.")
        break