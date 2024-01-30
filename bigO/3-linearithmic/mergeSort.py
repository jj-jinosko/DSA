# Time Complexity: O(nlogn)
# merge two ORDERED ARRAYS?

def mergeSort(arr):
    n = len(arr)
    if n < 2: # is it better to use < 2, ==1, or >1 here?
        print('arr', arr)
        return arr
    mid = n // 2
    left = arr[:mid]
    print('left', left)
    right = arr[mid:n] # note that splice is up to but not including n, and index is length - 1
    print('right', right)
    return merge(mergeSort(left), mergeSort(right))

def merge(leftArr, rightArr):
    resultArr = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] <= rightArr[rightIndex]:
            resultArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            resultArr.append(rightArr[rightIndex])
            rightIndex +=1

    if leftIndex < len(leftArr):
        resultArr.append(leftArr[leftIndex])
    if rightIndex < len(rightArr):
        resultArr.append(rightArr[rightIndex])
    
    return resultArr
    # return resultArr.append(leftArr[:leftIndex].append(rightArr[rightIndex]))

arr = [12, 3, 16, 6, 5, 1]

print(mergeSort(arr))

# Q: can the input arrays be different lengths?
            
# Q: int() vs math.floor() vs ceil()?
#   A: int() is same as math.floor() for positive values
#       same as ceil() for negative values
#   A: can use floor division operator! //
            
