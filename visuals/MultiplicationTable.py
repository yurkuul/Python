"""
Prints a 9 x 9 multiplication table.

@author: Lisa
@Python version: Python 3.8.10
@version: 0.0.2
"""

def printHeader():
    """
    Prints the row header for the multiplication table
    """
    header = ""
    for i in range (1, 10):
        header += "\t{}".format(i)
    header += "\n"
    return header

def printTable(rowNum):
    """
    Prints the table for the multiplication table
    """
    theTable = ""
    for column in range(1, 10):
        theTable += str(rowNum * column) 

print(printHeader())
for row in range(1, 10):
    print(row)
    print()