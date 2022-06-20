def isPal(x: int) -> bool:
    return str(x) == str(x)[::-1]



num = 1
print(isPal(num))
num = 10
print(isPal(num))
num = 101
print(isPal(num))
num = -1
print(isPal(num))