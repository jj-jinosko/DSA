
# basic anagram review first, hashmap soln
input1 = "cat"
input2 = "act"

def isAnagram(input1, input2):
    # check length
    if len(input1) != len(input2):
        return False
    
    # create dict{letter: count}
    letters1, letters2 = {}, {}

    # Time = O(2n) 
    # for letter in input1:
    #     letters1[letter] = 1 + letters1.get(letter, 0)
    # for letter in input2:
    #     letters2[letter] = 1 + letters2.get(letter, 0)
    
    # Time = O(n), can combine loops by using index instead
    for i in range(len(input1)):
        letters1[input1[i]] = 1 + letters1.get(input1[i], 0)
        letters2[input2[i]] = 1 + letters2.get(input2[i], 0)

    
    # compare dictionaries
    for key in letters1:
        if letters1[key] != letters2.get(key, 0):
            return False
    print('True')
    return True

isAnagram("cat", "act")

arr1 = ["cat", "act", "eat", "ate", "tea"]

def groupAnagrams(arr):

    # create dictionaries of AlphabetCountKey:words
    anagramDict = {}
    for word in arr1:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord("a")] += 1
        # print(word)
        # print(count)
        countKey = tuple(count)
        # check if key is in dictionary
        if countKey in anagramDict: # if anagramDict[countKey]: doesn't work bc throws keyerror, not true/false
            # anagramDict[countKey] = [anagramDict[countKey], word]
            # anagramDict[countKey] = list(anagramDict[countKey]).append(word)
            # print(type(anagramDict[countKey])) //
            anagramDict[countKey].append(word)
        else:
            anagramDict[countKey] = [word]
    print(anagramDict)
    anagramGroups = []
    for key in anagramDict:
        anagramGroups.append(anagramDict[key])
    
    return anagramGroups
        
print(groupAnagrams(arr1))

# [['cat', 'act'], ['eat', 'ate', 'tea']]


