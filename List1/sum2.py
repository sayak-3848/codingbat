## Given an array of ints, return the sum of the first 2 elements
# in the array.
# If the array length is less than 2,
# just sum up the elements that exist,
# returning 0 if the array is length 0.

def sum2(nums):
    return sum(nums[:2])

print(sum2([1,2,3]))
print(sum2([1,1,1,1]))
print(sum2([9,8,7,6]))
