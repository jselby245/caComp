# Task 1
# Josh Selby 2016

# Asks user for a sentence:
sentence = input("Please enter a sentence to process: ")

# Asks user for a word to find in that sentence:
word = input("Please enter a word to find in the sentence: ")

# Splits the sentence into a list
sentenceList = sentence.split()

# List for storing word positions:
wordPosList = []

# Looks for postions that word appears in the sentence:
for i, j in enumerate(sentenceList): # For every object (j) in the list
    if j == word: # If the word given by the user is the same as the word the program is currently looking at
        wordPosList.append(i)

# Prints the result:
print(wordPosList)