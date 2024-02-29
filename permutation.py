# reverse a string
# related: palindrome checker

# flip a string
# remember, a string is immutable, so we have to create a new string to store the flipped string in


# flip a string with recursion
def permute(word, pocket=""):
    if len(word) == 0:
        print(pocket)
    else:
        for i in range(len(word)):
            letter = word[i]
            left = word[0:i]
            right = word[i+1:]
            together = left + right
            permute(together, letter+pocket)

# Time complexity O(n!)?
# Space complexity
        
print(permute("AB",""))

# reverse a string with slicing
myWord = "hello"

newWord = myWord[::-1] #olleh
skipWord = myWord[::2] #hlo
leftWord = myWord[:3] # hel, up to but not including 3
rightWord = myWord[3:] # lo
print(myWord[0])
print(newWord)
print(skipWord)
print(leftWord)
print(rightWord)

# flip a string with iteration


# reverse a string with reverse

def search(arr, target):
    for element in arr:
        if element == target:
            return "Found!"
        else:
            return "not found... =["
        
def searchAgain(arr, target):
    for i in range(len(arr)): 
        if arr[i] == target:
            return "Found!"
        else:
            return "not found... "