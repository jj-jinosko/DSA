# Assigning vs copying!!!

row1 = ['a', 'b', 'c', 'd', 'c']
row2 = row1.copy()
row3 = row1
row2.sort()
row3.sort()

# print(myRow.sort())
print(row1)
print(row2)
print(row3) # row3 AND row1 refer to the same exact list, so when row3 gets sorted, it's sorting the list referred to as row1 and row3

print(id(row3))
print(id(row1))
print(id(row2))