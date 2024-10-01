words = ["neet", "code"]

def encodeCipher(words):
    secret = ""; 
    for word in words:
        # print(secret)
        # print(len(word))
        secret = secret + str(len(word)) + ";" + word
    # print(secret)
    return secret

# need to use while loop bc the length of the words may be a variable number of digits (not just 1 digit)
# def decodeCipher1(secret):
#     # words = secret.rsplit("") # won't work bc number changes
#     # iterate through each character and evaluate?

#     # want to always start with first number
#     words = []
#     for i in range(len(secret)):
#         print("i:", i)
#         print("secret[i]:", secret[i])
#         if i == 0:
#             letterCount = int(secret[i])
#             word = secret[i+1:i+1+letterCount]
#             print(word)

#         elif i == letterCount + 1: # location of next letterCount
#             print("testing")
#             # print(i)
#             # print(secret[i])

#             letterCount = letterCount + int(secret[i])

#         print('letterCount', letterCount)
        
        
# def decodeCipher(secret):
#     words = []
#     i = 0 #this is my pointer

#     while i < len(secret):
#         j = i
#         print("i", i)
#         print("j", j)
#         while secret[j] != ";":
#             j += 1
#             # print(secret[i:j])
#         length = int(secret[i:j])
#         print('length', length)
#         word = secret[j + 1 : j + 1 + length]
#         print('word', word)
#         words.append(word)
#         i = j + 1 + length
#         j = i
#     return words




def decodeCipher(secret):
    words = []
    i = 0
    # print(len(secret))
    while i < len(secret):
        print("loop")
        j = i
        while secret[j] != ";":
            j += 1
        # print("j", j)
        length = int(secret[i:j])
        # print(length)
        # the following three lines can be rewritten, setting the pointer i = j + 1 and j = i + length
        word = secret[j + 1 : j + length + 1]
        words.append(word)
        i = j + length + 1
    return words
        
        

        # wordLength = secret[i:j]
        # print("wordLength", wordLength)
        

test = "hello"
print(test[:4]) # up to but not including index 4
# mystery = encodeCipher(words)
# print(mystery)

# print(decodeCipher(mystery))
print(decodeCipher("4;neet4;code"))



############ SECRET SECRET SAUCE #################################
# https://medium.com/@ozoniuss/leetcode-encode-and-decode-strings-a-different-approach-533fcd5b6888

def encodeBonus(secret):
    code = ""
    for word in secret: 
        for letter in word:
            code = code + letter * 2
            # print(code)
        code = code + "01"
    return code

def decodeBonus(hidden):
    words = []
    word = ""
    for i in range(0, len(hidden) - 1, 2):
        if hidden[i] == hidden[i+1]:
            word = word + hidden[i]
        else:
            words.append(word)
            word = ""
    return words



message = encodeBonus(["lil", "squeeze"])
print(decodeBonus(message))

# for i in range(0, 10, 2):
#     print(i)
#     print('hello')

