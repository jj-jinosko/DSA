# Algorithms to calculate the factorial of a number

# input: num = positive integer
# ouput: num!

# iterative
def factorial(num):
    for i in range(num+1):
        # print('this is i', i)
        if i == 0: #bc range starts at 1
            ans = 1
        else:
            ans = ans * i
            print('ans', ans)
    return ans


print(range(4))
print(range(1, 4))

# iterative simple
def factorialSimple(num):
    ans = 1
    for i in range(1, num+1):
        ans = ans * i
    return ans

# recursive
def factorialRE(num):
    if num == 0:
        return 1
    else:
        return num * factorialRE(num - 1)
    # return factorialRE(ans)



# -------tests--------
print(factorialSimple(3)) #6
# print(factorial(4)) #24
# print(factorial(5)) #120

# print(factorialRE(3)) #6