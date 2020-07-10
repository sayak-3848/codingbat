## Given an array of ints length 3,
# return an array with the elements
# "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
    return nums[1:] + [nums[0]]

print(rotate_left3([1,2,3]))
print(rotate_left3([1,11,1111]))
print(rotate_left3([5,7,9]))
