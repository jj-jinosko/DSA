# https://www.techiedelight.com/find-number-rotations-circularly-sorted-array/
# Find the number of rotations of a circularly sorted array

# the lowest value is the "pivot point", 
# the index value of the pivot point, indicates the number of rotations 
# it is the only value where the value to the left and right are larger than it

# a fully sorted array will not contain the pivot point
# Therefore, if the left and right value of a subarray are low and high, respectively,
# if cannot containt the pivot point, and we can throw that side out

# Input:
arr1 = [8, 9, 10, 2, 5, 6]
arr2 = [2, 5, 6, 8, 9, 10]

# Output 
# The array has been rotated x times  = index of pivot point

# linearSearchRotations ------------------------
def linearSearchRotations(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1] and arr[i] < arr[i-1]:
            return i
print("linear search rotations")
print(linearSearchRotations(arr1))
print(linearSearchRotations(arr2))

# binarySearchRotations ------------------------
print("binary search rotations")

def binarySearchRotations(arr):
    left = 0
    right = len(arr) - 1
    
    # if search space is already sorted
    if arr[left] <= arr[right]: # if array was only one item long, this would still return index 0
        return left
    
    while left <= right:
        mid = left + (right - left) // 2
        print("left", left)
        print("mid", mid)
        print("right", right)

        # find the next and previous element of the `mid` element (in circular manner)
        prev = (mid - 1 + len(arr)) % len(arr)
        next = (mid + 1) % len(arr)
        print(prev, mid, next)

        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        # search left side if right is sorted and mid is less than right
        elif arr[mid] < arr[right]: # can we used arr[left] > arr[mid] bc left not sorted? I think so... no because
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

print(binarySearchRotations(arr1))
# print(binarySearchRotations(arr2))




