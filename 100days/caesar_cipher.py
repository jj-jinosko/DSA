# Caesar cipher

# ===================== FLOW ========================

# take input
# encode or decode?
# message
# shift #
# algo
# output


# ====================== LESSONS ========================

# this is really a string manipulation problem
# ord() funtion to covert a letter to a number
# arr.append()
# ''.join(arr)

# ======================== MVP ========================

# def cipher():
#     print("Welcome to CIPHER")
#     setting = input("encode or decode? ")
#     msg = input("please input your message: ")
#     shift = int(input("please input the shift value: "))
#     hidden = []

#     print("calculating...")

#     if setting == "decode":
#         shift = -shift
#         print("shift value", shift)

#     for i in range(len(msg)): 
#         print("letter", msg[i], ord(msg[i]))
#         hidden.append(ord(msg[i]) + shift)
    
#     for i in range(len(msg)):
#         hidden[i] = chr(hidden[i])

#     print("hidden", hidden)
#     print(f"your message is: {''.join(hidden)}")



# cipher()

# rudqjh



# ======================== Improved ========================
# evaluate to None bc this function does not "return" data
# add defaults to inputs
# "".join(
    #     chr(ord(char) + shift)
    #     for char in msg
    # )


def cipher() -> None:
    print("Welcome to CIPHER")
    setting = input("encode or decode? ") or "encode"
    msg = input("please input your message: ") or "orange"
    shift = int(input("please input the shift value: ") or "3")
    hidden = []

    if setting == "decode":
        shift = -shift

    print("calculating...")

    result = "".join(
        chr(ord(char) + shift)
        for char in msg
    )
    print(result)

cipher()

# ====================== EVEN BETTER ==========================

print("Welcome to CIPHER")
setting = input("encode or decode? ") or "encode"
msg = input("please input your message: ") or "orange"
shift = int(input("please input the shift value: ") or "3")

def caesar(msg: str, shift: int) -> str:
    return "".join(chr(ord(c) + shift) for c in msg)


caesar(msg, shift)


