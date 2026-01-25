arr = [1, 2, 3, 4, 5] # assume sorted

def minMaxSum(arr):
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    print(min_sum)
    print(max_sum)

minMaxSum(arr)

def minMaxSum1(arr):
    total = min = max = 0
    for i in range(len(arr)):
        total += arr[i]
    
    min = total - arr[-1]
    max = total - arr[0]
    print(min)
    print(max)

minMaxSum1(arr)

def minMaxSum2(arr):
    total = sum(arr)
    print(total - arr[-1])
    print(total - arr[0])

minMaxSum2(arr)


# if arr isn't sorted

def minMaxSum3(arr):
    total = sum(arr)
    print(total - max(arr)) # min
    print(total - min(arr)) # max

# min max are built-ins, so use different names

