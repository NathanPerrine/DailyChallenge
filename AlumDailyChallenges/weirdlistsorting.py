# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
# Example 2:
# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]


import collections 
def weirdListThing(l1, l2):
    c = collections.Counter(l1)
    newList = []
    for num in l2:
        if num in c:
            newList.extend([num] * c[num])
            del c[num]

    for k, v in c.items():
        newList.extend([k] * v)
    return(newList)



arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(weirdListThing(arr1, arr2))
print('[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]')

print('--------------------')


arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(weirdListThing(arr1, arr2))
print('[22, 28, 8, 6, 17, 44]')