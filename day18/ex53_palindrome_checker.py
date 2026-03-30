# Initialize variable to store the word
word = ""

print("\n=== Palindrome Checker ===")
print("Enter a word to check if it is a palindrome.")
print("Type 0 to exit the program.\n")

while True:

    # Ask the user to enter a word
    word = input("Enter a word: ")

    # Exit condition
    if word == "0":
        print("\nProgram terminated.")
        break
    
    # Normalize the word to lowercase
    word = word.lower()
    
    # Reverse the word using slicing
    reverse_word = word[::-1]

    

    # Check if the word is equal to its reversed version
    if word == reverse_word:
        print("Result: This is a palindrome.\n")
    else:
        print("Result: This is not a palindrome.\n")