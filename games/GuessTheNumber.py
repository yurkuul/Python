import random

"""
Guess the number game.

@author: LZ-FSDev
@Python version: Python 3.9
@version: 0.0.5
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
print("Setting up your game...")

difference = highRange - lowRange
if (difference > 5):
    guesses = difference // 5
else:
    guesses = 1

number = random.randint(lowRange, highRange)
stillGuessing = True

print("A random number has been created within the range of {} and {}. You have {} guess(es). Goodluck!".format(lowRange, highRange, guesses))
print()

guess = int(input("Enter your guess: "))

while (guesses > 0 and stillGuessing):
    difference = guess - number
    if (guess == number):
        print("You win!")
        stillGuessing = False
    elif (guess < lowRange or guess > highRange):
        print("That's outside the guessing range!")
    elif (difference <= 10 and difference > 0):
        guesses -= 1
        print("You are within 10 digits above the number!")
    elif (abs(difference) <= 10):
        guesses -= 1
        print("You are within 10 digits below the number!")
    print()
    if (guesses == 0):
        print("You were unable to guess the number :( Better luck next time!")
        print("The number was " + str(number) + ".")
        stillGuessing = False
    elif (stillGuessing):
        print("You have {} guesses left.".format(guesses))
        guess = int(input("Enter your guess: "))
        print()
