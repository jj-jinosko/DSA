arr = [-1, 55, 9, 10, 5]

# find max element in array

# ------------------BUILT IN SEARCH, MAX------------------
# Time complexity : O(n log(n)) # loop is n, log(n) is ?
# Auxiliary Space : O(1)

# use max() function
print(max(arr))

# use sorted() function + index
arrSorted = sorted(arr) # sorted doesn't modify arr
print(arrSorted[-1])

# use .sort() method + index
newArr = arr
newArr.sort() # modifies newArr
print(newArr[-1])

# ------------------LINEAR SEARCH variations------------------
# Time Complexity: O(n)
# Auxiliary Space: O(1), as no extra space is used

# linear search + max() function
def getMax0(arr, n):
    result = arr[0]
    for i in range(1, n): #can start at 1 bc already assigned first element to result
        result = max(result, arr[i])
    return result

print(getMax0(arr, len(arr)))

# 
def getMax(arr):
    result = arr[0]
    for element in arr:
        result = max(result, element)
    return result

print(getMax(arr))

## what is the time complexity here? for the if statement? I think constant
def getMax2(arr):
    result = arr[0]
    for element in arr:
        if element > result:
            result = element
    return result

print(getMax2(arr))

# Recursive Solution
# what is the point of doing this?
print("Recursive Soln")
def getMaxRecursive(arr, n): 
    if(n==1):
        return arr[0]
    # If there is single element, return it. 
    # Else return maximum of first element 
    # and maximum of remaining array. 
    else:
        print(max(getMaxRecursive(arr[1:], n-1), arr[0]))
        return max(getMaxRecursive(arr[1:], n-1), arr[0])
 
# Driver code
n = len(arr)

print("Maximum element of array: ", getMaxRecursive(arr, n))