import random

"""
Guess the number game.

@author: LZ-FSDev
@Python version: Python 3.9
@version: 0.0.2
"""

print("Welcome to Guess The Number!")
print()

lowRange = int(input("Insert the lowest value you would like to guess from: "))

highRange = int(input("Insert the highest value you would like to guess from: "))

while (highRange < lowRange):
    print("That is lower than your lowest value!")
    highRange = int(input("Insert the highest value you would like to guess from: "))

print()

number = random.randint(lowRange, highRange)
stillGuessing = True

print("A random number has been created within the range of {} and {}. Start guessing!".format(lowRange, highRange))
print()

guess = int(input("Enter your guess: "))

while (stillGuessing):
    if (guess == number):
        print("You win!")
        break
    if (guess < lowRange or guess > highRange):
        print("That's outside the guessing range!")
        print()
    guess = int(input("Enter your guess: "))
    print()