arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def sumDiags(arr):
    # print(arr[0][-4]) # IndexError
    n = len(arr)
    first = 0
    second = 0
    for i in range(n):
        first += arr[i][i]
        second += arr[i][-(i+1)]
    return abs(first - second)

print(sumDiags(arr))