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