import random

"""
Guess the number game.

@author: LZ-FSDev
@Python version: Python 3.9
@version: 0.0.6
"""

print("Welcome to Guess The Number!")
print()

choosingNumber = True #holds on to if user is still choosing a value

lowRange = input("Insert the lowest value you would like to guess from: ")

#keep asking for a valid integer if input is not an integer
while (not lowRange.isnumeric()):
    print("That is not a value!")
    lowRange = input("Insert the lowest value you would like to guess from: ")
print()

#cast a valid integer as the lowest value to guess from
lowRange = int(lowRange)

highRange = input("Insert the highest value you would like to guess from: ")

#keep asking for a valid integer if input is not an integer
while (choosingNumber):
    if (not highRange.isnumeric()):
        print("That is not a value!")
        highRange = input("Insert the highest value you would like to guess \
            from: ")
    #checks to see if high value is not lower than low value
    elif (int(highRange) < lowRange):
        print("That is lower than your lowest value!")
        highRange = input("Insert the highest value you would like to guess \
            from: ")
    else:
        #if highest value is chosen, stop asking for values
        choosingNumber = False

#cast a valid integer as the highest value to guess from
highRange = int(highRange)

print()
print("Setting up your game...")

#algorithm for choosing how many guesses the user gets
"""
within the range of the lowest value to highest value inclusive, every 5
values equal 1 guess for the user
i.e. lowest value = 50, highest value = 60, the difference is 60-50 = 10
and 5 fits into 10 twice, so the user gets 2 guesses
"""
difference = highRange - lowRange
if (difference > 5):
    guesses = difference // 5
else:
    #if the difference is not larger than 5, user gets at least 1 guess
    guesses = 1

number = random.randint(lowRange, highRange)
stillGuessing = True #holds on to if user is still allowed to guess

print("A random number has been created within the range of {} and {}. You \
have {} guess(es). Goodluck!".format(lowRange, highRange, guesses))
print()

guess = int(input("Enter your guess: "))

#checks to see if user is still guessing
while (guesses > 0 and stillGuessing):
    difference = guess - number #how far the guess is from the value
    if (guess == number): #if user has guessed the number
        print("You win!")
        stillGuessing = False
    #makes sure the user is guessing within the lowest to the highest values
    elif (guess < lowRange or guess > highRange):
        print("That's outside the guessing range!")
    #checks to see if the user is at least 10 digits above the number
    elif (difference <= 10 and difference > 0):
        guesses -= 1
        print("You are within 10 digits above the number!")
    #checks to see if the user is at least 10 digits below the number
    elif (abs(difference) <= 10):
        guesses -= 1
        print("You are within 10 digits below the number!")
    print()
    if (guesses == 0): #checks to see if user is out of guesses
        print("You were unable to guess the number :( Better luck next time!")
        print("The number was " + str(number) + ".")
        stillGuessing = False
    elif (stillGuessing): #keep asking user for input if still guessing
        print("You have {} guesses left.".format(guesses))
        guess = int(input("Enter your guess: "))
        print()
