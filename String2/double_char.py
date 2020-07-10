## Given a string, return a string where for every char
## in the original, there are two chars.

def double_char(str):
    result = ""
    for i in range(len(str)):
        result = result + str[i] * 2
    return result

print(double_char("The"))
print(double_char("Nandini"))
print(double_char("Hello"))
