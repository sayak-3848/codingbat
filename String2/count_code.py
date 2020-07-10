## Return the number of times that the string "code"
## appears in the given string, except we will accept
## any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
    count = 0
    for i in range(len(str)):
        if  str[i:i+2]=="co" and str[i+3:i+4]=="e":
            count = count + 1
    return count

print(count_code("aaacodebbb"))
print(count_code("codexxxcode"))
print(count_code("cozexxxxcope"))
