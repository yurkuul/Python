import random

"""
Guess the number game.

@author: LZ-FSDev
@Python version: Python 3.9
@version: 0.0.3
"""

print("Welcome to Guess The Number!")
print()

choosingNumber = True

lowRange = input("Insert the lowest value you would like to guess from: ")

while (not lowRange.isnumeric()):
    print("That is not a value!")
    lowRange = input("Insert the lowest value you would like to guess from: ")
print()

lowRange = int(lowRange)

highRange = input("Insert the highest value you would like to guess from: ")

while (choosingNumber):
    if (not highRange.isnumeric()):
        print("That is not a value!")
        highRange = input("Insert the highest value you would like to guess from: ")
    elif (int(highRange) < lowRange):
        print("That is lower than your lowest value!")
        highRange = input("Insert the highest value you would like to guess from: ")
    else:
        choosingNumber = False

highRange = int(highRange)

print()

number = random.randint(lowRange, highRange)
stillGuessing = True

print("A random number has been created within the range of {} and {}. Start guessing!".format(lowRange, highRange))
print()

guess = int(input("Enter your guess: "))

while (stillGuessing):
    if (guess == number):
        print("You win!")
        stillGuessing = False
    if (guess < lowRange or guess > highRange):
        print("That's outside the guessing range!")
        print()
    guess = int(input("Enter your guess: "))
    print()
