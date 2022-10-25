"""
Prints a 9 x 9 multiplication table.
@author: Lisa
@Python version: Python 3.8.10
@version: 0.0.3
"""

def getHeader():
    """
    Returns the row header for the multiplication table
    """
    header = ""
    for i in range (1, 10):
        header += "\t{}".format(i)
    header += "\n"
    return header

def getRow(rowNum):
    """
    Returns the row for the multiplication table
    """
    theRow = ""
    for column in range(1, 10):
        theRow += str(rowNum * column) + "\t"
    return theRow

print(getHeader())
for row in range(1, 10):
    print(str(row) + "\t", end="")
    print(getRow(row))
    print()
