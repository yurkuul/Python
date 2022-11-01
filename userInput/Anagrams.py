word1 = input("Please enter a word: ")
word2 = input("Please enter a second word: ")
dict1 = dict()
dict2 = dict()
isAnagram = True
keyValue = 0 #holds on to the key of each value inputted

#adding each letter of word1 with a keyValue to a dict
for i in range(len(word1)):
    dict1[keyValue] = word1[i:i+1]
    keyValue+=1

keyValue = 0 #resetting the key value to 0

#adding each letter of word2 with a keyValue to a dict
for i in range(len(word2)):
    dict2[keyValue] = word2[i:i+1]
    keyValue+=1
    
#check if dict1 and dict2 contain the same values
for i in dict1.values():
    if i not in dict2.values():
        isAnagram = False

if isAnagram:
    print("The two words entered are anagrams.")
else:
    print("The two words entered are not anagrams.")
