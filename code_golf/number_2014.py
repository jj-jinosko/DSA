# https://codegolf.stackexchange.com/questions/17005/produce-the-number-2014-without-any-numbers-in-your-source-code


# tests
myString = "—"

result = myString.encode()
num = int.from_bytes(result, byteorder='big')
print(num)

# Using the Unicode escape sequence
em_dash = '\u2014'
test = '\u2017'
text = "This" + em_dash + "works everywhere."
print(text)

huh = ord('-')
check = chr(2014)

# You can also use it directly within a string
text_unicode = f"Here is an em dash \u2014 it's {test} easy {huh}!"
print(text_unicode)
print(check)



# my solution

print(ord('ߞ'))

# alt