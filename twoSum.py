arr = [1, 2, 4, 5, 7, 9]
arr2 = [1, 1, 1, 1, 1]
target = 9

# brute force, check every combination of values
# def twoSumDup(arr, target):
#     n = len(arr)
#     for i in range(n):
#         print(i)
#         for j in range(n):
#             print(j)
#             if arr[i] + arr[j] == target and i != j:
#                 return f"{arr[i]} + {arr[j]} = {target}, are found at indexes {i} and {j}, respectively"
            
# brute force +, reduce checking values again, by checking only values that come after the index being checked
def twoSumDup(arr, target):
    n = len(arr)
    for i in range(n):
        # print("i", i)
        for j in range(i+1, n): # start second index check after i
            # print("j", j)
            if arr[i] + arr[j] == target:
                return f"{arr[i]} + {arr[j]} = {target}, are found at indexes {i} and {j}, respectively"
            

# assuming that the arrays are sorted already
def twoSumPointers(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        if (arr[left] + arr[right]) == target:
            return arr[left], arr[right]
        elif (arr[left] + arr[right]) > target:
            right = right - 1
        elif (arr[left] + arr[right]) < target:
            left = left + 1
    return "no soln found"

print(twoSumPointers(arr, 9))
print(twoSumPointers(arr2, 9))

# hashmap, regardless of sorted status
# secret sauce, target - element = value. Check if value exists as key in hashmap

def twoSumHashExists(arr, target):
    hash = {}
    for element in arr:
        num = target - element
        # print(hash[num])
        print(hash)
        if num in hash: 
            return True #this just finds if the value exists, but doesn't retain the original index information
        hash[element] = num


print(twoSumHashExists(arr, target))

def twoSumHashIndex(arr, target):
    n = len(arr) # n = 6
    prevMap = {}
    for i in range(n): #range(6) => 0, 1, 2, 3, 4, 5
        # print('index', i)
        diff = target - arr[i] 
        if diff in prevMap:
            return i, '+', prevMap[diff]

twoSumHashIndex(arr, target)


#====================================================================================


nums1 = [7,3,4,5,6]
target = 7

def twoSum(nums, target):
    # first, sort the arr if necessary
    orderedNums = sorted(nums)
    # print(orderedNums)
    # check left and right elements, move based on result compared to target until left === right
    left = 0
    right = len(orderedNums) - 1
    while left <= right:
        print(orderedNums[left], orderedNums[right])
        if orderedNums[left] + orderedNums[right] == target:
            return orderedNums[left], "+", orderedNums[right], "==", target
        elif orderedNums[left] + orderedNums[right] <= target:
            left = left + 1
        elif orderedNums[left] + orderedNums[right] >= target:
            right = right - 1
    
    return 'no match'
        


print(twoSum(nums1, target))


# play w enumerate
def enumPlay(nums, target):
    # first, create a dict
    numsMap = {}

    for idx, num in enumerate(nums, 1):
        print(f"Hello, {idx} is num {num}")

enumPlay(nums1, target)


# twoSum w hashmap (no duplicate values)
# why no duplicate values? because, if there are no duplicate values, we can create a hashmap of the array values, and check if the key exists

def twoSumHash(nums, target):
    # first, create a dict
    numsMap = {}

    for idx, num in enumerate(nums):
        diff = target - num
        # print(idx, num)
        if num in numsMap:
            print(f"Values {num} + {diff} = {target} and are found at indexes {numsMap[num]} and {idx}, respectively")
        numsMap[diff] = idx

twoSumHash(nums1, target)



