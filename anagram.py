# input: "god", "dog"
# output: true

# convert string to array
# sort arrays
# compare arrays

def compareArrays(input1, input2):
    arr1 = []
    arr2 = []
    for letter in input1:
        arr1.append(letter)
    arr1.sort()
    for letter in input2:
        arr2.append(letter)
    arr2.sort()

    n = len(arr1)
    m = len(arr2)
    if n != m:
        print(False)
    else:
        for i in range(n):
            if arr1[i] != arr2[i]:
                print(False)
        print(True)

    print(arr1)
    print(arr2)


compareArrays("go", "dog")

# create letter count using dictionaries (hashmap)

def countLetters(input1, input2):
    letterDict = {}
    for letter in input1:
        if letter in letterDict:
            letterDict[letter] += 1
        else:
            letterDict[letter] = 1
    print(letterDict)

countLetters("god", "dog")



# 
def isAnagram(input1, input2):
    # check lengths first
    if len(input1) != len(input2):
        return False
    
    # create dictionaries (hashmaps)
    count1, count2 = {}, {}
    for i in range(len(input1)):
        # print(input1[i])
        # count1[input1[i]] += 1 #if key doesn't exist yet, will throw a KeyError
        # count1[input1[i]] = 1 + count1[input1[i]] # same as above
        count1[input1[i]] = 1 + count1.get(input1[i], 0)
        count2[input2[i]] = 1 + count2.get(input2[i], 0)
    # compare dictionaries
    for key in count1: 
        # if count1[key] != count2[key]:  #if count2[key] is not found, will throw KeyError
        if count1[key] != count2.get(key, 0):
            return False
    print("True")
    return True

isAnagram('god', 'ppl')


#

# isAnagram?
word1 = "god"
word2 = "dog"

# brute force, compare each letter O(n^2)
# does this handle duplicate values? I don't think so... oh wait, check the length
# still... is there something like ggod and ddog that would be a false positive? I think so
# I guess it has to be sorted first
def isAnagram1(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        n = len(word1)
        # res = False
        for i in range(n):
            for j in range(n):
                print("check")
                print(word1[i], word2[j])
                if word1[i] == word2[j]:
                    continue
                
                
# array: create sorted array of letters and compare 
def isAnagram2(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        arr1 = []
        arr2 = []
        for i in range(len(word1)):
            arr1.append(word1[i])
            arr2.append(word2[i])
        arr1.sort()
        arr2.sort()
        print(arr1, arr2)
        if arr1 == arr2:
            return True
        else:
            return False

print(isAnagram2(word1, word2))

# dictionary: create dictionary of letters w lettercount and compare

# python cheat is string.sort()
def isAnagram0(word1, word2):
    print(sorted(word1))
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

print(isAnagram0(word1, word2))

# group anagrams
words = ["god", "dog", "eat", "tea"]
# 