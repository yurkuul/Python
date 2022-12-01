def recursiveSum(inputList):
    if len(inputList) == 1:
        return inputList[0]
    elif len(inputList) > 1:
        return inputList[-1] + recursiveSum(inputList[0:len(inputList)-1])
    else:
        return -1

list1 = [1,2,3,4,5,6]

print(recursiveSum(list1))
