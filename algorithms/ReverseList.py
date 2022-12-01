aList = [5, 8, 2, 6, 9, 3, 4]
newList = list()

def reverseList(inputList):
    if len(inputList) == 1:
        newList.append(inputList[0])
    elif len(inputList) > 1:
        newList.append(inputList[len(inputList)-1])
        return reverseList(inputList[0:len(inputList)-1])
    return newList

reversedList = reverseList(aList)

print("original list:", aList)
print("reversed list:", reversedList)
