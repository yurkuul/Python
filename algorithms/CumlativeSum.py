def cumulativeSum(inputList):
    if len(inputList) == 1:
        return inputList[0]
    elif (len(inputList) > 1):
        sumList.append(inputList[0] + inputList[1])
        inputList[1] = inputList[0] + inputList[1]
        return cumulativeSum(inputList[1:])
    else:
        return -1
    
sumList = list()

testList = [5, 8, 2, 6, 9, 3, 4]

sumList.append(testList[0])

cumulativeSum(testList)

print(sumList)
