# import random

# def lcm_naive(a, b):
#     for l in range(1, a * b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     assert False

def lcm(a, b):
    #first find gcd of a and b
    # print('got here')
    gcd_result = gcd(a, b)
    # print('got here')
    #lcm = (gcd)(a/gcd)(b/gcd)
    # print(int(a*b/gcd_result))
    return (int(a*b/gcd_result))

def gcd(a,b):
    if b == 0:
        return a
    else:
        c = a % b
    return gcd(b, c)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

#--------- sanity check -----------------
# test1 = [18, 12] #36
# test2 = [20, 5] #20
# print('test1')
# print(lcm_naive(*test1))
# print(lcm(*test1))
# print('test2')
# print(lcm(*test2))
# print(lcm_naive(*test2))

#--------- stress test -------------
# def StressTest():
#     for i in range(50):
#         # generate random number from 
#         num1 = random.randrange(1, 1000) + 2
#         num2 = random.randrange(1, 10000) + 2
#         # print(num)
#         res1 = lcm_naive(num1, num2)
#         res2 = lcm(num1, num2)
        
#         # if res1 == res2:
#         #     print("sweet")
#         #     print('lcm(', num1, ', ', num2, ')')
#         #     print(res1, res2)
#         # else:
#         #     print("nooooo", res1, res2)

#         if res1 != res2:
#             print('noooo', res1, res2)

# print(StressTest())