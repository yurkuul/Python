"""
Prints a triangle of values corresponding to the row.

@author: Lisa
@version: Python 3.9
"""

rows = input("Enter how many rows you want for your triangle:")

rowNumber = 1

for x in range(int(rows)):
    for y in range(rowNumber):
        print (rowNumber, end= ' ')
    print()
    rowNumber += 1
