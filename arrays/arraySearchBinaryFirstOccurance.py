# https://www.techiedelight.com/find-first-or-last-occurrence-of-a-given-number-sorted-array/
# Find the first or last occurrence of a given number in a sorted array
# Given a sorted integer array, find the index of a given number’s first or last occurrence. 
# If the element is not present in the array, report that as well.

# binary search for target value
# binary search again to left for first occurrence, to right for last occurrence

# 11:44
# implemented regular binary search for target in 7 minutes

def findFirstTarget(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        # if target is less than mid value, discard right side
        elif target < arr[mid]:
            right = mid - 1
        
        # if target is greater than mid value, discard left
        else:
            left = mid + 1

    return result


def findLastTarget(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        print("index:", left, mid, right)
        print("value:", arr[left], arr[mid], arr[right])
        if arr[mid] == target:
            result = mid
            left = mid + 1 # continue searching to right
            print("mid value is same as target value, continue search to right")
        # if target is less than mid value, discard right side
        elif target < arr[mid]:
            right = mid - 1
            print("mid value is greater than target value, remove right")
        # if target is less than mid value, discard left
        else:
            left = mid + 1
            print("mid value is less than target value, remove left")

    return result
        
# Input: 
arr1 = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 5

print(findFirstTarget(arr1, target))
print(findLastTarget(arr1, target))