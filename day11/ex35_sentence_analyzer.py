# Ask the user to insert a sentence
word = input("Insert a sentence: ")

# Remove extra spaces from the beginning and end
clean_sentence = word.strip()

# Display the cleaned sentence
print("Sentence without spaces at start/end:", clean_sentence)

# Display the sentence in uppercase
print("Sentence in uppercase:", clean_sentence.upper())

# Show the total number of characters
print("Total characters:", len(clean_sentence))