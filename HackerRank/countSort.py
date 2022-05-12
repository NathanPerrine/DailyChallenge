import random
def countingSort(arr):
    countSort = [0] * 100
    
    for num in set(arr):
        countSort[num] = arr.count(num)
    
    return countSort




l1 = []
for x in range(1, 50):
    l1.append(random.randint(0, 25))
print(countingSort(l1))