# SearchDuplicateUnsorted.py
# https://neetcode.io/problems/duplicate-integer


# arr = [1, 2, 3, 4, 5, 5]
arr = [3, 2, 1, 3, 5, 6, 7]
arr2 = [1, 2, 3, 1]

# brute force 
# compare two values in every combination (lxw)
# Time: O(n^2)
# Space: 
def searchDuplicateNaive(arr):
    n = len(arr)
    for i in range(n - 1): 
        # print("i", arr[i])
        for j in range(n):
            # print("j", arr[j])
            if arr[i] == arr[j] and i != j:
                return True
    return False

print(searchDuplicateNaive(arr))
        
def searchDuplicateBetterNaive(arr):
    n = len(arr)
    for i in range(n-1):
        # print("i", i)
        for j in range(i+1, n): # doesn't check values redundantly
            # print("j", j)
            if arr[i] == arr[j]:
                return True
    return False

print(searchDuplicateBetterNaive(arr))

# sort the array: O(nlogn) using sort() function
# compare adjacent values: O(n)   
# n = len(arr)       
# for i in range(n-1):
#     if arr[i] == arr[i+1]:
#         print("true")

def sortSearchDuplicate(arr):
    print("sortSearchDuplicate: ")
    n = len(arr)
    arrSorted = sorted(arr)
    print(arrSorted)
    for i in range(n-1):
        if arrSorted[i] == arrSorted[i+1]:
            return True
    return False
print(sortSearchDuplicate(arr))

# create dictionary, check for element in dictionary during creation
def dictDuplicate(arr):
    myDict = {}
    n = len(arr)
    for element in arr:
        if element in myDict:
            print("myDict", myDict)
            print(element, "already in myDict")
            return True
        myDict[element] = "exists"
    return False

print("DICT")
print(dictDuplicate(arr))

# create hashset, then check for duplicates
# create hashet O(n) space complexity
# check hashset if value exists: O(n) time complexity
def setSearchDuplicate(arr):
    hashset = set()
    for element in arr:
        if element in hashset: # search set O(n)
            return True
        hashset.add(element) # create set O(n)
    return False

print("\nHASHSET")
print(setSearchDuplicate(arr))