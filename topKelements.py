arr = [1, 2, 2, 3, 3, 3]
# topK(arr, 2) => [2, 3] bc 2 and 3 occur 2+ times

# arrK = []

# for i in range(len(arr)):
#     # print('i', i, arr[i])
#     if arr[i] in arrK:
#         print(arr[i], 'in array already')
#     else:
#         count = 1
#         for j in range(len(arr)):
#             # print('j', j, arr[j])
#             # print(count)
#             if arr[i] == arr[j] and i != j:
#                 count += 1
#                 # print(arr[i], "=", arr[j])
#                 # print('count', count)
#             if count == 2 and arr[i] not in arrK:
#                 arrK.append(arr[i])
#                 print(arrK)


# top k elements
# return the list of numbers from a list of integers that occur at least k times

# nums = [1, 2, 2, 2, 3, 3, 3, 3, 3]
# def findCountMatch(nums, k):
#     countMatch = []

#     for i in range(len(nums)-1):
#         print('i', i)
#         print(nums[i])
#         # print('count', count)
#         # if number is same as next consecutive, add to count
#         if nums[i] == nums[i+1]:
#             count += 1
#         # if number is not same as next consecutive, but same as previous, check count against k
#         elif nums[i] == nums[i-1]:
#             if count >= k:
#                 countMatch.append[nums[i]]
#         else:
#             count = 0
#     print(countMatch)


# findCountMatch(nums, 2)


# def findCountMatch(nums, k):
#     kCount = []
#     count = 1
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i+1]:
#             count += 1
#             if count == k and (nums[i] not in kCount): 
#                 kCount.append(nums[i])
#                 count = 1 # if you just don't reset the count here there won't be a need to check if the num is already in the list
#         else:
#             count = 1
#     print(kCount)


# findCountMatch(nums, 2)



nums = [1, 2, 2, 2, 3, 3, 3, 3, 3]

def findCountMatch(nums, target):
    ans = []
    count = 1
    for i in range(len(nums) - 1): # use length nums - 1 bc checking nums[i+1] 
        if nums[i] == nums[i+1]:
            count += 1
        else:
            count = 1
        if count == target:
            ans.append(nums[i])
    return ans

print(findCountMatch(nums, 2))
