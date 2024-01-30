# linearithmic
# O(nlogn)

# --------- iterative ---------------
print('ITERATIVE')
def linearithmic(n):
    y = n
    while n > 1:
        arr = []
        n = n / 2
        # print('n', n)
        for i in range(y):
            arr.append(i)
        print(arr)

# linearithmic(4)
# linearithmic(5)
# linearithmic(6)
linearithmic(8) # 8xlog_2(8) = 8x3 = 24

# --------- recursive ---------------
print('\nRECURSIVE')
def nlognR(n, y):
    arr = []
    n = n / 2
    for i in range(y):
        arr.append(i)
    print(arr)
    if n > 1:
        nlognR(n, y)

print(nlognR(8, 8))


#------- building an array in a recursive function -----------

# print('\nRECURSIVE')
# def nlognR(n, y, arr):
#     if arr is None:
#         arr = []
#     n = n / 2
#     for i in range(y):
#         arr.append(i)
#     print(arr)
#     if n > 1:
#         nlognR(n, y, arr)

# # arrR = [] # DO NOT PASS EMPTY ARRAY AS ARGUMENT!! https://www.codiga.io/blog/python-avoid-empty-array-parameter/
# arrR = None
# print(nlognR(8, 8, arrR))

