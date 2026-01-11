import random

# ------- generate fib modulos
# fibList = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393]
# def find_mods(arr1, mod):
#     arr2 = []
#     for i in arr1:
#         arr2.append(i % mod)
#     return arr2

# print(find_mods(fibList, 2))
# print(find_mods(fibList, 3))
# print(find_mods(fibList, 4))
# print(find_mods(fibList, 5))
# ------------------------------------

# def fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m


# find the period of fib(n)%m and save as array
# def fibonacci_period(n, m):
#     fib = [0, 1]
#     period = [0, 1]
#     repeat = False

#     while repeat == False:
#         #compute fib n
#         fib.append(fib[-2] + fib[-1])
#         # now fib has another value added
#         previous = fib[-2] % m
#         current = fib[-1] % m
#         period.append(current)

#         if previous == 0 and current == 1:
#             repeat = True
#     # print(fib)
#     return period[:-2]

def fibonacci_period(n, m):
    fib = [0, 1]
    period = [0, 1]
    repeat = False

    while repeat == False:
        #compute fib n
        fib = fibFinder(fib)
        # now fib has another value added
        previous = fib[-2] % m
        current = fib[-1] % m
        period.append(current)

        if previous == 0 and current == 1:
            repeat = True
    # print(fib)
    return period[:-2]

def fibFinder(fib):
    fib.append(fib[-2] + fib[-1])
    return fib

# print('10 and 2')
# print(fibonacci_period(10, 2))
# print('10 and 3')
# print(fibonacci_period(10, 3))
# print('10 and 4')
# print(fibonacci_period(10, 4))

def fibonacci_number(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] +  arr[i-2])
    return arr[n]

def fibonacci_huge(n, m):
    period = fibonacci_period(n, m)
    # print(period)
    periodLength = len(period)
    # print(periodLength)
    # fibNum = fibonacci_number(n)
    # print(fibNum)
    # print('n', n)
    index = (n % periodLength)
    # print('index', index)
    num = period[index]
    return num
    
#---------- sanity check --------
# print(fibonacci_huge(6,2)) #0
# print(fibonacci_huge(6,3)) #2
# print(fibonacci_huge(6,4)) #1


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))


#--------- test -----------------
# test1 = [6, 2] #0
# test2 = [6, 3] #2

# print('test1')
# print(fibonacci_huge_naive(*test1))
# print(fibonacci_huge(*test1))
# print('test2')
# print(fibonacci_huge_naive(*test2))
# print(fibonacci_huge(*test2))


#--------- stress test -------------
# def StressTest():
#     for i in range(500):
#         # generate random number from 2-50
#         num = random.randrange(1, 48) + 2
#         # print(num)
#         res1 = fibonacci_huge_naive(num)
#         res2 = fibonacci_huge(num)
        
#         # if res1 == res2:
#         #     print("sweet")
#         # else:
#         #     print("nooooo", res1, res2)

#         if res1 != res2:
#             print('noooo', res1, res2)

# print(StressTest())