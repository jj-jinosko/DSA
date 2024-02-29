# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
expenses = [2200, 2350, 2600, 2130, 2190]


# 1. In Feb, how many dollars you spent extra compare to January?
print(expenses[1] - expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print(expenses[0] + expenses[1] + expenses[2])

# 3. Find out if you spent exactly 2000 dollars in any month
# search
print("2000 in expenses", 2000 in expenses)
# for i in expenses:
#     if i == 2000:
#         print('spent 2000')
# else:
#     print('didnt spend 2000 even')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# insert
#expenses[5] = 1980 #IndexError bc this memory location doesn't exist yet!
expenses.append(1980)
print(expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] = expenses[3] - 200
print(expenses)


# ----------------------
heroes = ['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heroes))
# 2. Add 'black panther' at the end of this list
# insert
heroes.append('black panther')
print(heroes)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heroes.pop()
# does the space still exist where black panther was? No
print(heroes[-1])
heroes.insert(3, 'black panther')
print(heroes)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# heroes[1:2] = 'doctor strange' # messes up insertion
heroes[1:3] = ['doctor strange']
print(heroes)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# print(dir(heroes))
heroes.sort()
print(heroes)


# ------------
# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user 
# using input() function
def makeOddList(num):
    oddList = []
    for i in range(1, num):
        if i % 2 == 1:
            oddList.append(i)
    return oddList

# print(makeOddList(10))
custom = int(input("enter a number: "))

print(makeOddList(custom))

