## Given an array of ints, return True if the array
## contains a next to a 2 somewhere.

def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
        else:
            return False

print(has22([1,2,2]))
print(has22([1,2,1,2]))
print(has22([2,1,2]))
