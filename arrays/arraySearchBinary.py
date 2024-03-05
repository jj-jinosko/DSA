# binary Search
# a target value can be found in a sorted array
# by dividing the array in two and comparing the mid value
# to the target value

# think of the example of finding a word in the dictionary

# Test Inputs
target = 5
arr = [1, 5, 8, 9, 100, 101, 105, 1000, 10001]

# Iterative Binary Search Function
# return index of target in array if present,
# else returns -1

def binarySearchIt(arr, target):
	lo = 0
	mid = 0
	hi = len(arr) - 1

	while lo <= hi:
		print("lo", lo, "hi", hi)
		mid = (lo + hi) // 2 # // floor division
		print("new mid", mid)
		# target is on the left side
		if arr[mid] > target:
			hi = mid - 1 # use -1 bc we don't need to check mid value again
		# target is on the right side
		elif arr[mid] < target: 
			lo = mid + 1
		else:
			return mid
			
print(binarySearchIt(arr, target))

# Iterative Binary Search Function
# https://www.geeksforgeeks.org/binary-search/
# It returns index of x in given array arr if present,
# else returns -1
# def binary_search(arr, x):
# 	low = 0
# 	high = len(arr) - 1
# 	mid = 0

# 	while low <= high: # why do we need to check low = high case?

# 		mid = (high + low) // 2

# 		# If x is greater, ignore left half
# 		if arr[mid] < x:
# 			low = mid + 1

# 		# If x is smaller, ignore right half
# 		elif arr[mid] > x:
# 			high = mid - 1

# 		# means x is present at mid
# 		else:
# 			return mid

# 	# If we reach here, then the element was not present
# 	return -1


# # Test array
# arr = [1, 2, 3, 5, 6]
# x = 4

# # Function call
# result = binary_search(arr, x)

# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")

# ---------------------------------------------------------------------
# practice reproduction of Iterative Binary Search

# Test Input
arr = [1, 2, 3, 5, 6]
x = 3

# Iterative Binary Search Function

def binarySearch(arr, target):
	lo = 0
	hi = len(arr) - 1
	mid = 0 # still not sure why we initialize here

	while lo <= hi: 
		mid = lo + (hi-lo)//2 # gets the midpoint index of the array, and avoids direct addition of lo + hi, which could cause overflow if the indexes were sufficiently large

		if arr[mid] > target:
			hi = mid - 1 
		elif arr[mid] < target:
			lo = mid + 1
		else:
			return mid
	return -1 # indicate that target was not found

# Function Call
print("-------------------------")
result = binarySearch(arr, x)
if result == -1:
	print("Your value was not found")
else:
	print("Your value was found at index: ", result)

# ---------------------------------------------------------------------