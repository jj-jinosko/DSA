import inspect
# Python does not techically have arrays
# Python lists can be used as arrays 
# to work with arrays in Python you will have to import a library, like the NumPy library.

# Structure: Arrays are collections of data that are linear and indexed
# In python there are four collection data types:
# list, tuple, set, dictionary

#------------- lists ---------------

# create a list with bracket notation or list constructor 

arr1 = ['a', 'b', 'c', 'd', 'e', 'f']
arr2 = list((5, 9, 4, 8)) # need double round brackets
# arr3 multiple data types

#-------------access list items----------------
# access items in an array with bracket notation and index number
# lists are indexed, starting at 0

# access one list item
print(arr1[0]) #a
print(arr2[-1]) #8

# access a range of list items
print(arr1[1:3]) # b c (up to but not including 3rd index)
print(arr1[:3]) # a b c (up to but not including 3rd index)
print(arr1[3:]) # d e f

print(arr1[-3:-1]) # d e (up to but not including last index)
print(arr1[-1:-3]) # prints empty array

# access items in an array with

# arrays are mutable, i.e. I can change the value at an index in an array

#--------------search---------------------------
thislist = ["apple", "banana", "cherry"]

# Python builtin check if item exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# search unsorted array
#
for item in thislist:
  if item == "apple":
    print("Yes, 'apple' is in the fruits list")

#
n = len(thislist)
for index in range(n):
  if (thislist[index] == "apple"):
    print("Yes, 'apple' is in the fruits list")


def findElement(arr, n, key):
    for i in range(n):
        if (arr[i] == key):
            return i
           
    # If the key is not found
    return -1

arr = [12, 34, 10, 6, 40]
key = 40
n = len(arr)
 
# search operation
index = findElement(arr, n, key)
if index != -1: ## why this check? maybe just so we can use if/else?
    print("Element Found at position: " + str(index + 1))
else:
    print("Element not found")
 
# Time Complexity: O(N) 
# Auxiliary Space: O(1)


#--------------insert operation----------------------------
# append, insert, extend, or custom function

# 1 insert at the end of an unsorted array
# only one operation
def insert(arr, element):
    arr.append(element) 
    return arr # append modifies the original array

print(insert(arr, 'apple')) # [12, 34, 10, 6, 40, "apple"]
# Time Complexity: O(1) 
# Auxiliary Space: O(1)

# 2 insert at any position in array
# one operation to insert, plus shift up to n characters = n+1
# Time Complexity: O(n) 
# Auxiliary Space: O(1)

# insert() method 
# modifies exising
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # ['apple', 'banana', 'watermelon', 'cherry']
print(thislist) 

# extend() method
# modifies exising
thistuple = ("kiwi", "orange")
print(type(thislist.extend(thistuple))) # class NoneType, bc method, not data 
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry', 'kiwi', 'orange']

# custom function
# first, we need to make sure that the array has available spaces for the new item.
# depending on the language data type, the array will have to have extra 'spaces'

# use range to increment back from the end of the list
for i in range(9, 2, -1):
   print(i)

def insertElement(arr, n, x, pos):
    for i in range(n-1, pos-1, -1):
       print('i', i)
       print('arr i', arr[i])
       arr[i + 1] = arr[i]
       print('new arr i', arr[i])
    arr[pos] = x

# here -1 is for empty space
arrInsert = [2, 4, 1, 8, 5, -1]
n = 5

insertElement(arrInsert, 5, 'surprise', 2)
print(arrInsert) # [2, 4, 'surprise', 1, 8, 5]
# arrInsert is modified, the -1 "space" at the end of the array was replaced by the previous shifted elements
# Time complexity: O(N)
# Auxiliary Space: O(1)

# insert into a sorted array
# first requires search (complexity depends on search alg)
# then, shift up to index (up to n shifts)
# then insert (1 operation)
    
#--------------remove----------------------------
# methods: pop(item at index), remove(item at index ?), del(), clear()
# custom

# replicate remove() method, remove an element at an unknown location 
# in an unsorted array
# first, search for the item, then delete item, then shift items over
print('\n')
print('removeElement')
def removeElement(arr, x):
    n = len(arr)
    delete = None
    for i in range(n-1):
        if arr[i] == x:
            delete = i
    if delete != None:
        for i in range(delete, n-2, 1):
           print(arr[i])
           arr[i] = arr[i+1]
           print('arr', arr)
    
    return arr

arrRemove = [10, 50, 30, 40, 20]
keyRemove = 30

print(removeElement(arrRemove, keyRemove))

# Python program to delete an element
# from an unsorted array
 
# Driver's code
if __name__ == '__main__':
    # Declaring array and key to delete
    arr = [10, 50, 30, 40, 20]
    key = 30
  
    print("Array before deletion:")
    print (arr)
  
    # deletes key if found in the array 
    # otherwise shows error not in list
    arr.remove(key)
    print("Array after deletion")
    print(arr)
#------------------------------------------
  
# sort, copy, join, loop