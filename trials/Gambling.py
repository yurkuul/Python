import numpy as np
import random

STARTING_MONEY = 100 #in dollars
GAMES = 1000

avgMoney = 0
netGainCount = 0
netGainPercentage = 0

def makeListOfFlips():
    return np.random.randint(0, 2, 50)

def runOneGame():
    #0 = heads, 1 = tails
    playerFlips = makeListOfFlips()
    dealerFlips = makeListOfFlips()
    playerAmount = STARTING_MONEY
    for i in range(50):
        if dealerFlips[i] == 1 and playerFlips[i] == 0:
            playerAmount += 2
        elif dealerFlips[i] == 0 and playerFlips[i] == 0:
            playerAmount -= 1
        elif playerFlips[i] == 1:
            playerAmount -= 1
    return playerAmount

def runGames():
    playerAmounts = np.zeros(GAMES)
    for i in range(GAMES):
        playerAmounts[i] = runOneGame()
    return playerAmounts

playerMoney = runGames()

for money in playerMoney:
    if (money > STARTING_MONEY):
        netGainCount += 1
    avgMoney += money
    
avgMoney /= GAMES
netGainPercentage = netGainCount / GAMES * 100

print("Average money from 1000 games:", avgMoney)
print("Net gain count:", netGainCount)
print("Net gain percentage:", netGainPercentage)
