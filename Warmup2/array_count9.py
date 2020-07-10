## Given an array of ints, return the number of 9's in the array

def array_count9(nums):
    total = 0
    for i in nums:
        if i==9:
            total = total + 1
    return total

print(array_count9([1,3, 9]))
print(array_count9([1,9,9]))
print(array_count9([1,9,9,3,9]))
