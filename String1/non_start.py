## Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(a,b):
    return a[1:] + b[1:]

print(non_start("Hello","there"))
print(non_start("python","code"))
print(non_start("Ilove","python"))