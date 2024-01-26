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


#--------------add----------------------------
#--------------remove----------------------------

#--------------search---------------------------
#check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")




#------------------------------------------
  
# sort, copy, join, loop