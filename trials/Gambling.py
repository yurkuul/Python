import numpy as np
import random

STARTING_MONEY = 100 #in dollars
GAMES = 1000 #the number of games for experimental data and analysis

avgMoney = 0 #the average amount of money the player has at the end
netGainCount = 0 #the number of times the player net gains
netGainPercentage = 0 #the percentage of times the player net gains

def makeListOfFlips():
    return np.random.randint(0, 2, 50)

def runOneGame() -> int:
    """
    Run a single game of gamble. Does 50 flips for both the player
    and the dealer and updates the player money amount based on the
    flips.
    """
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

def runGames() -> array:
    """
    Runs the gamble game GAMES amount of times and stores all player
    amounts into an array.
    """
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
