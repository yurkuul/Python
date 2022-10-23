"""
Prints a triangle of values corresponding to the row.

@author: Lisa
@version: Python 3.9
@version 0.0.2
"""

def getTriangle(rows):
    """
    Returns the current row of numbers for the pyramid
    """
    theRow = ""
    for i in range(1, int(rows)+1):
        theRow += str(i) + " "
    return theRow

rows = input("Enter how many rows you want for your triangle: ")

for i in range(int(rows)+1):
    print(getTriangle(i))
