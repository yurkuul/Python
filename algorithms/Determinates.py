import numpy as np

def det2(array):
    """
    Calculates the determinate of a 2x2 matrix.
    [[a  b]
     [c  d]]
    determinate = ad-bc
    
    Parameter array is a 2x2 array.
    
    Returns the determinate of a 2x2 matrix.
    """
    return array[0][0] * array[1][1] - array[0][1] * array[1][0]

def det3(array):
    """
    Calculates the determinate of a 3x3 matrix.
    [[a  b  c]
     [d  e  f]
     [g  h  i]]
    determinate = (ei-fh) - (di-fg) + (dh-eg)

    Parameter array is a 3x3 array.
    
    Returns the determinate of a 3x3 matrix.
    """
    cofact1 = array[1:3, 1:3]
    cofact2 = array[1:3, :3:2]
    cofact3 = array[1:3, :2]
    return det2(cofact1) - det2(cofact2) + det2(cofact3)
    
def addMatrices(array1, array2):
    """
    Calculates the sum of 2 matrices. Matrices must be of the same size.
    
    Parameter array1 and array2 are matrices that are size mxn.
    
    Returns the sum of the 2 matrices. -1 if sizes are different.
    """
    sumArray = np.zeros((len(array1), len(array1[0])))
    if len(array1) != len(array2) or len(array1[0]) != len(array2[0]):
        return -1
    for row in range(len(array1)):
        for column in range(len(array1[row])):
            sumArray[row][column] = array1[row][column] + array2[row][column]
    return sumArray
            

#MAINLINE
array1 = np.zeros((3, 3))
array2 = np.zeros((3, 3))
value = 1
for i in range(len(array1)):
    for j in range(len(array1[i])):
        array1[i][j] = value
        array2[i][j] = value
        value += 1

print("Original array:")
print(array1)
print("---------------------------")

print("Determinate of a 3x3 array:")
print(det3(array1))
print("---------------------------")
print("Adding two 3x3 matrices:")
print(addMatrices(array1, array2))
