# https://www.geeksforgeeks.org/find-lost-element-from-a-duplicated-array/

# Find a lost element in a duplicated array
# assume unsorted ==> linear search or sort first
# assume arr1 or arr2 could be the shorter array
# assume only one value is missing

arr1 = [1, 4, 5, 7, 9]
arr2 = [4, 5, 7, 9]

# linear search
# this solution checks everything
# Time complexity: O(n^2)
def findMissingDuplicateNaive(arr1, arr2):
    if len(arr2) > len(arr1):
        longer = arr2
        arr2 = arr1
        arr1 = longer
    for item in arr1:
        found = False
        for element in arr2:
            if item == element:
                found = True
                break # we don't need to keep checking after this
        if found == False:
            return item

print("missing item:", findMissingDuplicateNaive(arr1, arr2))


# assume input arrays are sorted

# binary search


