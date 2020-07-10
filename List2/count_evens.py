## Return the number of even ints in the given array.
## Note: the % "mod" operator computes the remainder
## eg. 5%2 is .

def count_evens(nums):
    count = 0
    for i in nums:
        if i%2 == 0:
            count = count + 1
    return count

print(count_evens([2,1,2,3,4]))
print(count_evens([2,2,0]))
print(count_evens([1,3,5]))
