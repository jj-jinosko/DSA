candles = [3, 2, 1, 3]

def birthdayCandles(arr):
    count = 0
    max_num = max(arr)
    for element in arr:
        if element == max_num:
            count += 1
    print(count)

birthdayCandles(candles)

# w no max() function
# have to sort arr

def birthdayCandles1(arr):
    count = 0
    max_num = 0
    for i in range(len(arr)):
        if arr[i] == max_num:
            count += 1
        if arr[i] > max_num:
            max_num = arr[i]
            count = 1
    print(count)

birthdayCandles1(candles)

def birthdayCandles2(arr):
    max_num = arr[0]
    count = 1

    for num in arr[1:]:
        if num == max_num:
            count += 1
        elif num > max_num:
            max_num = num
            count = 1

    print(count)

birthdayCandles2(candles)

# default w first num as max in arr