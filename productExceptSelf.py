# https://neetcode.io/problems/products-of-array-discluding-self

nums = [1, 2, 4, 6]
# res = [48, 24, 12, 8]

prefix = [1]
postfix = [1]
pre = 1
post = 1
ans = []

for num in nums:
    pre = pre * num
    # print(pre)
    prefix.append(pre)
print(prefix)

for i in range(len(nums) - 1, -1, -1):
    # print("hello?")
    # print("i", i)
    post = post * nums[i]
    postfix.append(post)
# postfix.append(1)
print(postfix)

for i in range(len(nums)):
    print("i: ", i)
    # print(prefix[i])
    # print(len(postfix)-i)
    # print(postfix[len(postfix)-i-2:len(postfix)-i-1])
    last = postfix[len(postfix)-i-2:len(postfix)-i-1]
    # last[0]
    prod = prefix[i] * last[0]
    print(prod)
    # print("ho")

# test = ["a", "b", "c", "d"]
# print(test[-2:-1])