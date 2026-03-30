# Ask the user to type a word and remove extra spaces
word = input("Choose a word: ").strip()

# Check if the user entered something
if word:
    
    # Show the first letter of the word
    print("First Letter:", word[0])

    # Show the last letter of the word
    print("Last Letter:", word[-1])

    # Show the word in uppercase
    print("Word in Uppercase:", word.upper())

    # Show the word in lowercase
    print("Word in Lowercase:", word.lower())

else:
    # Message if the user does not type anything
    print("You did not enter a word.")