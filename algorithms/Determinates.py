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

#MAINLINE
array1 = np.zeros((3, 3))
value = 1
for i in range(len(array1)):
    for j in range(len(array1[i])):
        array1[i][j] = value
        value += 1

print("Original array:")
print(array1)
print("---------------------------")
