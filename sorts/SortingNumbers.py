import numpy as np

np.random.seed(1012)

DATASIZE = 1000 #number of values in the array
MAX_VALUE = 10000000 #max value for the integers in the array

data = np.random.randint(0, MAX_VALUE, size=DATASIZE) #array of rand integers

def sortArray(array):
    """
    Sorts the array by going through each element in the array. Checks if the
    next element is smaller than the current and if it is, swap the elements.
    
    Parameter 'array' is the array used for sorting.
    """
    for i in range(len(array)-1):
        if (array[i+1] < array[i]):
            tempVal = array[i]
            array[i] = array[i+1]
            array[i+1] = tempVal
    
def sortArrayOfSize(numTimes):
    """
    Calls the sortArray() 'numTimes' times.
    
    Parameter 'numTimes' is the number of times sortArray() is called.
    """
    while (numTimes > 0):
        sortArray(data)
        numTimes -= 1


#MAINLINE
sortArrayOfSize(DATASIZE)
