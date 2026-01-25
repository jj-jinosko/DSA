arr = [-4, 3, -9, 0, 4, 1]

def ratioNums(arr):
    n = len(arr)
    pos = neg = zer = 0
    # pos, neg, zer = 0, 0, 0

    for i in range(n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        elif arr[i] == 0: # elif w else as valueError good for production code, not necessary for hackerRank
            zer += 1
    posRatio = round(pos/n, 6)
    negRatio = round(neg/n, 6)
    zerRatio = round(zer/n, 6)

    print(posRatio) # 3 / 6
    print(negRatio) #
    print(zerRatio)
    # return posRatio, negRatio, zerRatio
    return None

ratioNums(arr)

# notes
# variables assigned to non-primative structure refer to EXACT same structure
# variables assigned to a primative structure are not 'synced up'


arr1 = ['a', 'b', 'c']

a = b = c = arr1

print("a", a)
a.append('d')
print("a", a)
print("b", b) #['a', 'b', 'c', 'd']

d = e = 0

d = d + 1
print('d', d, 'e', e)