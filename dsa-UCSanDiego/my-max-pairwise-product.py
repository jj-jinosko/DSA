import random

# def maxPairwiseProductNaive(arr):
#     product = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if product < arr[i] * arr[j]:
#                 product = arr[i] * arr[j]
#     return product

# if __name__ == '__main__':
#     _ = int(input()) # not sure why we need this
#     input_numbers = list(map(int, input().split()))
#     print(maxPairwiseProductNaive(input_numbers))


## search for 2 max numbers, then multiply
# def maxPairwiseProductFast(numbers):
#     num1 = numbers[0]
#     for i in numbers[1:]:
#         print(i)
#         if i > num1:
#             num1 = i
#             # print("num1 = ", num1)

#     if num1 == numbers[0]:
#         num2 = numbers[1]
#     else:
#         num2 = numbers[0]

#     for i in numbers:
#          if i > num2:
#              num2 = i
#             #  print("num2 = ", num2)

#     return num1 * num2
## doesn't work bc both numbers are max


def maxPairwiseProductFast(numbers):
    n = len(numbers)
    index1 = 0
    # num1 = numbers[index1]
    
    for i in range(n):
        if numbers[i] > numbers[index1]:
            index1 = i
            # num1 = numbers[index1]
            # print("num1 = ", num1)

    if index1 == 0:
        index2 = 1
        # num2 = numbers[1]
    else:
        index2 = 0
        # num2 = numbers[0]

    for i in range(n):
         if numbers[i] > numbers[index2] and i != index1:
             index2 = i
            #  print("num2 = ", numbers[index2])

    return numbers[index1] * numbers[index2]

# test1 = [1, 2, 3, 4, 5]
# test2 = [5, 4, 3, 2, 1]
# print(maxPairwiseProductFast(test1))
# print(maxPairwiseProductFast(test2))
# print(maxPairwiseProductNaive(test1))
# print(maxPairwiseProductFast(test2))

# ------------- stress test -----------------

# def StressTest():
#     for i in range(5):
#         arr1 = []
#         # generate random range from 2-11
#         n = random.randrange(1, 10) + 2
#         for i in range(n):
#             arr1.append(random.randrange(1,100))
#         # print(arr1)
#         res1 = maxPairwiseProductNaive(arr1)
#         res2 = maxPairwiseProductFast(arr1)
        
#         if res1 == res2:
#             print("sweet")
#         else:
#             print("nooooo", res1, res2)

# print(StressTest())

if __name__ == '__main__':
    _ = int(input()) # not sure why we need this
    input_numbers = list(map(int, input().split()))
    print(maxPairwiseProductFast(input_numbers))
