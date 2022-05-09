import itertools
def closestNumbers(numbers):
    differences = {}
    for a, b in itertools.combinations(numbers, 2):
            differences[a, b] = (abs(a-b))

    smallestDiff = min(list(filter(lambda x: x != 0, differences.values())))
    diff = [list(x) for x in differences.keys() if differences[x] == smallestDiff]

    for l in diff:
        l.sort()
    diff.sort()
    return diff

# numbers = []
# numbers = [6,2,4,10]
# numbers = [4, 4, 2, 1, 3]
numbers = [4, 4, -2, -1, 3]
print(closestNumbers(numbers))