# https://www.techiedelight.com/search-element-circular-sorted-array/

# find a target value in a rotated array

# figure out which side of the array is sorted
# figure out if target value is inside of the range on the sorted side

# Binary Search Rotated Array for target

def binarySearchRotatedTarget(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        print("left, mid, right", left, mid, right)
        print("left, mid, right", arr[left], arr[mid], arr[right])
        if arr[mid] == target:
            return mid
        
        # is right side sorted?
        if arr[mid] <= arr[right]: # we need to check = because mid and left or right could end up being the same value
            # is target between mid and right values?
            if arr[mid] <= target and target <= arr[right]:
                # search the right side
                left = mid + 1
                print("search right")
            # target is not between mid and right values
            else:
                right = mid - 1
                print("search left")
        # left side is sorted
        else:
            # is target between left and mid values?
            if arr[left] <= target and target <= arr[mid]:
                # search the left side
                right = mid - 1
                print("search left")
            else:
                left = mid + 1
                print("search right")
    return -1


# Input:
arr1 = [8, 9, 10, 2, 5, 6]
arr2 = [2, 5, 6, 8, 9, 10]
# arr1 = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 2, 5, 6]
# Output 
# Index of the target value:

# Function Call
result = binarySearchRotatedTarget(arr1, 9)
print("in arr1, 9 is at index: ", result)

