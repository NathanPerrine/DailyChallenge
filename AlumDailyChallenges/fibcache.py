from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    for i in range(400):
        print(i, fib(i))

if __name__ == "__main__":
    main()