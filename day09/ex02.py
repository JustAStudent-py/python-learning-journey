# Get input from the user
user_input = input("Choose a word: ")

# Convert input to uppercase to standardize processing
formatted_word = user_input.upper()

# Define vowels for comparison
VOWELS = "AEIOU"

# Iterate through each character in the word
for character in formatted_word:

    # Check if the character is a vowel
    if character in VOWELS:
        print(f"{character} <-- Vowel")

    # Check if the character is a digit
    elif character.isdigit():
        print(f"{character} <-- Number")

    # Check if the character is a letter (consonant)
    elif character.isalpha():
        print(f"{character} <-- Consonant")

    # Any other character is considered special
    else:
        print(f"{character} <-- Special character")