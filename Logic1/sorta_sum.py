## Given 2 ints, a and b, return their sum. However,
## sums in the range 10..19 inclusive, are forbidden,
## so in that case just return 20.

def sorta_sum(a,b):
    if a+b<10:
        return a+b
    elif a+b>20:
        return a+b
    else:
        return 20

print(sorta_sum(3,4))
print(sorta_sum(9,4))
print(sorta_sum(11,11))
