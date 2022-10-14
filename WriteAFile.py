# -*- coding: utf-8 -*-
"""
Grabs user input and appends to a file. Once the file closes, the number of
lines, words, and characters from the file will be printed.

@author: Lisa
@Python version: Python 3.8.10
@version: 0.0.2
"""

userFile = open("user_file.txt", "w")
lines = 1
words = 0
characters = 0
totalLines = 0
totalWords = 0
totalCharacters = 0

print("Welcome to Write-A-File!")
print("------------------------")

print("This is a demo for writing to a text file and to print out the " \
      "analytics of the file created.")
    
print("----------------------------------------------------------------------")

print("As the user, you will be creating the file via input you provide.")

print("We will provide the number of lines, words, and characters based " \
      "on your input.")

theLine = input("You may begin adding to the file. Type 'q' to quit: ")
    
while (theLine != 'q'):
    userFile.write(theLine + "\n")
    theLine = input("new line: ")

userFile.close()

print("-----------------------------------------------")

userFile = open("user_file.txt")

for line in userFile:
    print("Line " + str(lines))
    print (line)
    lines+=1
    totalLines+=1
    totalWords += len(line.strip().split())
    for character in line:
        totalCharacters +=1

print("----------------------------------------------------------------------")

print("The file that you just created has {} lines.".format(totalLines))
print("From those lines, you have {} words.".format(totalWords))
print("Your file contains {} characters, including white spaces."
      .format(totalCharacters))
