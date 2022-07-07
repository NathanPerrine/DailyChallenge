# Factorial 5 = 5 * 4 * 3 * 2 * 1 == 5!

def factorial(n):
    count = 1 
    for i in range(1, n+1):
        count *= i
    return count
print(factorial(10))


def recursiveFactorial(n):
    if n == 1:
        return n
    return n * recursiveFactorial(n-1)

print(recursiveFactorial(5))