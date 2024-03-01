# search for any occurrance of an adjacent duplicate
# i.e. the duplicate is next to the first occurrance of the element
# (not described very well, but still: https://www.geeksforgeeks.org/last-duplicate-element-sorted-array/)

# because we're only searching for items that are next to each other,
# we don't have to search every combination of two elements

# linear search!
# Time Complexity: O(n), one for loop that goes through every element
# Auxiliary Space: O(1), as no extra space is used.

arr = [1, 5, 5, 6, 6, 7]
# arr = [1, 0, 2, 3, 1, 7] # note that the 1 duplicates are not adjacent so they do not count
n = len(arr)

for i in range(n-1): # starts at 0, goes up to but doesn't include n. 
                    # bc we're going to check arr[i+1], we use range(n-1) so we don't end up checking an index that doesn't exist
    if arr[i] == arr[i+1]:
        print("Adjacent duplicate", arr[i+1], "found at index", i+1)


def findFirstAdjacentDuplicate(arr):
    for i in range(n-1): # starts at 0, goes up to but doesn't include n. 
                    # bc we're going to check arr[i+1], we use range(n-1) so we don't end up checking an index that doesn't exist
        if arr[i] == arr[i+1]:
            print("ADJACENT duplicate", arr[i+1], "found at index", i+1)
            return 
    print('no ADJACENT duplicate found')

print("Using the function we created")
findFirstAdjacentDuplicate(arr)

# # remember how range works!
# for i in range(6): # prints 0 1 2 3 4 5
#     print(i)