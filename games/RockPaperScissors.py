# -*- coding: utf-8 -*-

import random

"""
A rock paper scissors game.

@author: LZ-FSDev
@Python version: Python 3.9
@version: 0.0.1
"""

print("Welcome to rock paper scissors!")
print()

userChoice = input("Please type in console what you would like to go: ")
print()

print("Rock, Paper, Scissors!")
print()

choices = ["Rock", "Paper", "Scissors"]

#generating random int between 0 and 2 inclusive
randomChoice = random.randint(0,2)

print("Computer: {} \nUser: {}".format(choices[randomChoice], userChoice))
