## Given 2 int arrays, a and b, each length 3, return a new array
## length 2 containing their middle elements.

def middle_way(a,b):
    return [a[1],b[1]]

print(middle_way([1,2,3], [4,5,6]))
print(middle_way([5,5,5],[3,6,7]))
print(middle_way([5,3,9],[1,4,5]))

