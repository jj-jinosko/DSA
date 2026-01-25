n = 6

def staircase(n):
    for i in range(1, n+1):
        # print('x' * i + '#')
        print(' ' * (n-i) + '#' * i)

staircase(n)