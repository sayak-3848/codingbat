## Return the number of times that the string "hi"
## appears anywhere in the given string.

def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i:i+2] == "hi":
            count = count + 1
    return count

print(count_hi("abc hi ho"))
print(count_hi("hi how are you"))
print(count_hi("hi Nandini hi  hi hi"))