# import random

# def fibonacci_last_digit_naive(n):
#     arr = [0, 1]
#     for i in range(2, n+1):
#         arr.append(arr[i-1] +  arr[i-2])

#     return arr[n] % 10

def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        temp = current % 10
        current = (previous + current) % 10
        previous = temp

    return current


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))

#--------- test -----------------
# test1 = 6 #8
# test2 = 12 #144 => 4
# print(fibonacci_last_digit_naive(test1))
# print(fibonacci_last_digit_naive(test2))
# print(fibonacci_last_digit(test1))
# print(fibonacci_last_digit(test2))

#--------- stress test -------------
# def StressTest():
#     for i in range(500):
#         # generate random number from 2-50
#         num = random.randrange(1, 48) + 2
#         # print(num)
#         res1 = fibonacci_last_digit_naive(num)
#         res2 = fibonacci_last_digit(num)
        
#         # if res1 == res2:
#         #     print("sweet")
#         # else:
#         #     print("nooooo", res1, res2)

#         if res1 != res2:
#             print('noooo', res1, res2)

# print(StressTest())