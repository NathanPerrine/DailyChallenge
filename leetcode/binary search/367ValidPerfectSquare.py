#Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false

def perfectSquare(num):
    num = num ** 0.5
    if num % 1 == 0:
        return True
    return False


n = 16
# print(perfectSquare(n))

#bin search

def binSquare(num):
    l = 0
    h = num 
    while (l <= h):
        mid = (h + l) // 2
        guess = mid * mid
        if guess == num:
            return True
        elif guess < num:
            l = mid + 1
        else:
            h = mid -1

    return False



n = 14
print(binSquare(n))