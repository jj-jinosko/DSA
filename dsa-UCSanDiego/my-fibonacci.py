# n 1 2 3 4 5 6 ...
# o 1 1 2 3 5 8 ...

# def FibonacciNaive(n):
#     num1 = 1
#     num2 = 1
#     if n <= 1:
#         return n
#     else:
#         for i in range(n-2):
#             fib = num1 + num2
#             num1 = num2
#             num2 = fib
#         return fib


def FibonacciFast(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]

# print(FibonacciNaive(10))
# print(FibonacciFast(5))