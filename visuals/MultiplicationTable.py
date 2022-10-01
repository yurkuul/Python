"""
Prints a 9 x 9 multiplication table.

@author: Lisa
@Python version: Python 3.8.10
@version: 0.0.1
"""

#print the row header
for i in range (1, 10):
    print("\t{}".format(i), end="")

print() #ends the header

for row in range(1, 10): #prints out the rows
    #print the column header
    print(str(row) + "\t", end="")
    for column in range(1, 10): #prints out the columns
        print(row * column, end = "\t") #tabs each value
    print() #ends each multiplication row
