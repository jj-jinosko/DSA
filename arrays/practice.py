# practice creating an algorithm to search a rotated array for a target value

# rotated array has sorted and unsorted side
# can determine sorted side, then check if value is within range

# Input:
arr1 = [8, 9, 10, 2, 5, 6]
arr2 = [2, 5, 6, 8, 9, 10]


def findTarget(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == target:
            return mid
        # right side is ordered
        if arr[mid] <= arr[right]: #use <= bc mid and right could end up being the same
            # if target in range, search this side
            if arr[mid] <= target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        # if arr[mid] >= arr[left]
        else:
            if arr[mid] >= target >= arr[left]:
                right = mid - 1
            else:
                left = mid + 1
    # if while loop doesn't return any value
    return -1

print(findTarget(arr1, 10))
print(findTarget(arr2, 10))

# now, how would this algorithm change it we were always searching for 
# the lowest value in the array? i.e. the pivot point, the number of rotations of array

# Trick: the pivot point is the only value where the number is less than the value to the left and right of it
# so, we can essentially simplify the previous algorithm, because we know that we 
# are never searching for a target value in between other values, we always just want the lowest
