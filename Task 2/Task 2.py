# Asks user for sentence:
sentence = input("Please enter a sentence to process: ")
# Splits sentence:
sentenceList = sentence.split()
# Creates list for storing words and a list to recreate the sentence from:
wordList = []
recreationList = []

# Processes sentence:
for i,j in enumerate(sentenceList):
    if len(wordList) == 0:
        print("Ok")

    else:
        print("Not Ok")