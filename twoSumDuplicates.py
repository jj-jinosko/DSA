# twoSumDuplicates
# This is a variation of the twoSum problem, where the input array of nums may contain duplicate values

# Assumptions: 
# what it there can be more than one soln?

# Input: 
# - unsorted array of integers 
# - target value
# Output: two values that sum to target, including index following format:
# - "Values x + y = target, found at indexes i and j, respectively"


arr1 = [2, 3, 4, 5, 1]
arr2 = [2, 3, 4, 5, 2] # contains duplicate value
arr3 = [1, 1, 3, 4, 5] # contains duplicate value that will be in soln for target = 4
target = 4

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
# def twoSumDup(arr, target):
#     n = len(arr)
#     for i in range(n):
#         # print("i", i)
#         for j in range(i+1, n): # start second index check after i
#             # print("j", j)
#             if arr[i] + arr[j] == target:
#                 return f"{arr[i]} + {arr[j]} = {target}, are found at indexes {i} and {j}, respectively"
            

# sort values, then two-pointer search for combination
# def twoSumDup(arr, target):
#     arrSorted = sorted(arr)
#     left = 0
#     right = len(arr) - 1 # - 1 to convert len to index 
#     while left <= right:
#         if arr[left] + arr[right] == target:
#             return f"{arr[left]} + {arr[right]} = {target}, are found at indexes {left} and {right}, respectively"
#         elif arr[left] + arr[right] <= target:
#             left += 1
#         else:
#             right -= 1

# two step, create hashmap, then check if keys combinations that = target are in hashmap
# def twoSumDup(arr, target):
    #

# combined, create hashmap while checking if key combinations that = target are in hashmap
def twoSumDup(arr, target):
    numMap = {}
    for i, num in enumerate(arr):
        diff = target - num
        print("num: ", num, "diff: ", diff)
        print(numMap)

        if diff in numMap: # check if key exists 
            # if diff == num and len(numMap[diff] > 2): # if duplicates add to target, check if there are two indexes for the same value
            #     # indexes wouldn't both be there if the current number being checked hasn't been added to the dict... so there's no issue, we just want to know what index to return if the diff value matches a num with more than one instance
                # return 
            if len(numMap[diff]) > 1:
                # print("length", len(numMap[diff]))
                # print(numMap[diff], numMap[diff][1])
                return f"{diff} + {num} = {target}, and are found at indexes {numMap[diff][0]} and {i}, respectively" # returns just the first result 
            return f"{diff} + {num} = {target}, and are found at indexes {numMap[diff]} and {i}, respectively" # because diff already in map, it means the index comes before current num
        # numMap[num] = i # overwrites existing key value 
        # if num in numMap: # only keeps first num index value
        #     continue
        if num in numMap: 
            numMap[num] = [numMap[num], i]
            print("duplicate entered")
        else:
            numMap[num] = i
            

print(twoSumDup(arr3, target))