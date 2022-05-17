def isBadVersion(n):
    bad = 4 # change as needed to test
    return True if n >= bad else False

def firstBadVersion(n: int) -> int:
    l, h = 1, n
    while (l <= h):
        mid = (l + h) // 2
        
        if isBadVersion(mid):
            h = mid - 1
        else:
            l = mid +1
    return l

print(firstBadVersion(4))