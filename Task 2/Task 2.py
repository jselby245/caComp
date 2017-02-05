#
# PyCompress (Compression Stage)
# Written by Josh Selby, finalized:   /02/2017
#
# -- THIS IS THE MAIN SECTION, HANDLING THE COMPRESSION --
wordList = [] # Creates list for storing words
wordNumberList = [] # Creates list for storing numbers assigned to words in wordList
recreationList = [] # Creates list for numbers from wordNumberList that sentence could be recreated from

# Asks user for sentence to process and splits it into a list
sentenceList = (str(input("Please enter a string to process: "))).split()

# Loop for every object in sentence list. i = position in list, j = object at that position
for i, j in enumerate(sentenceList):
    if len(wordList) == 0: # Checks if wordList is empty
        wordList.append(j) # Word list is empty so will append first word in sentenceList
        wordNumberList.append(0) # Because wordList empty, wordNumberList must be empty so appends a zero
        # Adds wordNumberList number for that word to recreationList
        recreationList.append(wordNumberList[wordList.index(j)])

    else: # If wordList not empty
        if j in wordList: # If current word (j) in wordList
            recreationList.append(wordNumberList[wordList.index(j)]) # Add words relevant number to recreationList

        elif j not in wordList: # If current word (j) not in wordList
            wordList.append(j) # Add current word to word list
            wordNumberList.append(wordList.index(j)) # Assign word a number and add it to the wordNumberList
            recreationList.append(wordNumberList[wordList.index(j)]) # Add words relevant number to recreationList

        else: print("ERROR") # Displays error in case anything bad happens

# -- THIS IS THE SAVE SECTION, THIS SAVES THE CONTENTS OF THE LISTS REQUIRED FOR THE FILE RECONSTRUCTION
saveFileName = str(input("Please enter a name to save the file as: ")) # Asks for file name
wordFile = open(saveFileName + '.pycwf', 'w')
for i, j in enumerate(wordList):
    wordFile.write(str(j) + '\n')
wordFile.close()
recFile = open(saveFileName + '.pycrf', 'w')
for i, j in enumerate(recreationList):
    recFile.write(str(j) + '\n')
recFile.close()
# -- END OF PROGRAM --