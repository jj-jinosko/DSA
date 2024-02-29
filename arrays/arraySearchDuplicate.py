# search ordered array for any duplicate values
# does order affect efficiency? 
# I don't think so because I think we still have to check every value...

# ------------------------------------- #
# Input : arr= [1, 5, 5, 6, 6, 7]
# Output : 
# First duplicate index: 2
# First duplicate item: 5
# ------------------------------------- #
#-----------PSEUDO
# start with first element, arr[0]
# for i = 1 to n
#    if (arr[i] == arr[i-1])
#         Print current element and its index.
#         Return

# If no such element found print a message of no duplicate found.



#---------------

# brute force
# linear search for each element in array
# that means ~O(n^2), technically it's less than n^2, nlogn?
arr = [1, 5, 5, 6, 6, 7]
arr = [1, 0, 2, 3, 1, 7]
n = len(arr)

dupIndex = None
dupElement = None
def findDuplicateFirst(arr, n):
    for i in range(n):
        print("i---------", i)
        for j in range(i+1, n):
            print("j", j)
            if arr[i] == arr[j]:
                # dupIndex = j
                # dupElement = arr[j]
                print("A duplicate element", arr[j], "has been found at index", j)
                return

findDuplicateFirst(arr, n)


print("findDuplicateLast")
def findDuplicateLast(arr, n):
    for i in range(n-1, 0, -1):
        print("i---------", i)
        print(arr[i])
        for j in range(i-1, -1, -1):
            print("j", j, arr[j])
            
            if arr[i] == arr[j]:
                # dupIndex = j
                # dupElement = arr[j]
                print("A duplicate element", arr[j], "has been found at index", j)
                return

findDuplicateLast(arr, n)

# for i in range(7, -2, -1):
#     print(i)


