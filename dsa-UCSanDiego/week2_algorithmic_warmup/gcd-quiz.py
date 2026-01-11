# import random

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

def gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        # print("remainder", c)
    return (gcd(b, c))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))


#--------- sanity check -----------------
# test1 = [10, 6] #2
# test2 = [20, 5] #5
# print('test1')
# print(gcd_naive(*test1))
# print(gcd(*test1))
# print('test2')
# print(gcd(*test2))
# print(gcd_naive(*test2))

#--------- stress test -------------
# def StressTest():
#     for i in range(50):
#         # generate random number from 
#         num1 = random.randrange(1, 100000) + 2
#         num2 = random.randrange(1, 100000) + 2
#         # print(num)
#         res1 = gcd_naive(num1, num2)
#         res2 = gcd(num1, num2)
        
#         # if res1 == res2:
#         #     print("sweet")
#         #     print('gcd(', num1, ', ', num2, ')')
#         #     print(res1, res2)
#         # else:
#         #     print("nooooo", res1, res2)

#         if res1 != res2:
#             print('noooo', res1, res2)

# print(StressTest())