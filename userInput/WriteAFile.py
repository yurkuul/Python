# -*- coding: utf-8 -*-
"""
Grabs user input and appends to a file. Once the file closes, the number of
lines, words, and characters from the file will be printed.

@author: Lisa
@Python version: Python 3.8.10
@version: 0.0.4
"""

userFile = open("user_file.txt", "w") #file user will to adding to
lines = 1 #holds on to the line number when reading the file
words = 0 #holds on to the words in each line
characters = 0 #holds on to the number of characters in each line
totalLines = 0 #holds on to total lines in the file
totalWords = 0 #holds on to total words in the file
totalCharacters = 0 #holds on to total characters in the file

print("Welcome to Write-A-File!")
print("------------------------")

print("This is a demo for writing to a text file and to print out the " \
      "analytics of the file created.")
    
print("----------------------------------------------------------------------")

print("As the user, you will be creating the file via input you provide.")

print("We will provide the number of lines, words, and characters based " \
      "on your input.")
    
#user's line
theLine = input("You may begin adding to the file. Type 'q' to quit: ")

#keep asking user for sentences until they type 'q'
while (theLine != 'q'):
    userFile.write(theLine + "\n") #writes user input to file
    theLine = input("New line: ")

#close the file
userFile.close()

print("-----------------------------------------------")

#reopen the file for reading
userFile = open("user_file.txt")

#goes through each line from the file
for line in userFile:
    print("Line " + str(lines)) #prints out line number
    print (line.strip()) #prints out the line from file
    characters = len(line.strip())
    words = len(line.split())
    print("This line has {} words and {} characters.".format(words,characters))
    lines+=1
    totalLines+=1
    totalCharacters += characters
    totalWords += words
    print()

print("----------------------------------------------------------------------")

print("The file that you just created has {} lines.".format(totalLines))
print("From those lines, you have {} words.".format(totalWords))
print("Your file contains {} characters, including white spaces."
      .format(totalCharacters))
