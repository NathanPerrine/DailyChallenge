def miniMaxSum(arr):
    lowest = arr[:]
    lowest.remove(max(arr))
    highest = arr[:]
    highest.remove(min(arr))
    print(sum(lowest))
    print(sum(highest))

l1 = [1,2,3,4,5]
miniMaxSum(l1)