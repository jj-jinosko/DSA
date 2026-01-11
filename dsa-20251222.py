#2sum

arr1 = [1, 2, 3, 2]
arr2 = [1, 2, 2, 3]

# brute force
# sorted 
def bruteTwoSum(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            print("duplicate")
            return True
    print("no duplicates")
    return False

# bruteTwoSum(arr2)

def dicTwoSum(arr):
    mydict = {}
    for key in arr:
        print("key", key)
        if key in mydict:
            print("duplicate")
        else:
            mydict[key] = "exists"


def dictTwoSum2(arr):
    mydict = {}
    for i in range(len(arr)):
        if arr[i] in mydict:
            print(f"duplicate found at index {arr[i]}")
        else:
            mydict[arr[i]] = i
    
        

dictTwoSum2(arr2)

def setTwoSum(arr):
    mySet = set()
    for item in arr:
        print("item", item)
        if item in mySet:
            print("duplicate exists")
            mySet.add(item) # just doesn't do anything?
        else:
            mySet.add(item)
    print("mySet", mySet)

setTwoSum(arr2)

# remembered, python print w f-strings
# for key in dict
# mySet.add(item), add fn is idempotent i.e. repeating the fn doesn't do anything different that doing it once


##
