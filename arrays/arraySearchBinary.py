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

# n = len(arr)
# lo = 0
# mid = int(n/2)

# print(arr[mid])

# if arr[mid] == target:
#     print(mid)
# elif arr[mid] > target:



# Iterative Binary Search Function
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



