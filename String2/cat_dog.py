## Return True if the string "cat" and "dog" appear the
## same number of times in the given string.

def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str)):
        if str[i:i+3]=="cat":
            cat_count = cat_count + 1
        if str[i:i+3]=="dog":
            dog_count = dog_count + 1
    return cat_count == dog_count

print(cat_dog("catdog"))
print(cat_dog("catcat"))
print(cat_dog("1cat1cadodog"))
