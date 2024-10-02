# take move from left to right in array, comparing current value to the values left of it. 
# move the value down if it's smaller
arr = [3, 4, 1, 2]
def selectionSort(arr):
    for i in range(1, len(arr)):
        position = i
        temp = arr[i]
        while position > 0 and arr[position - 1] > temp:
            # print(i)
            # print(position)
            # check all indexes in arr
            # index starts at 1 bc comparison to i-1
            # move value until it's the min in comparison
            arr[position] = arr[position-1]
            arr[position-1] = temp
            position -= 1 # decrement to get out of while loop
    return arr

print(selectionSort(arr))
