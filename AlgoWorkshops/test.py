# given a list of integers and lists, reursively print each value
# in order from left to right

# example: [1,2,3,4,5,[6,7,8],[9,10,11], 12]
# should print
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# 11
# 12

l1 = [1,2,3,4,5,[6,7,8],[9,10,11], 12]

def recPrint(alist):
    if len(alist) == 1:
        return alist[0]
    if isinstance(alist[0], list):
        return recPrint(alist[0]) 

    return f"{alist[0]}{recPrint(alist[1:])}"


print(recPrint(l1))