# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


def isHappy(n: int) -> bool:
    memo = set()
    while n != 1:
        # Turn the number into a string, loop through the string adding the square of its digits
        n = sum([int(x) ** 2 for x in str(n)])

        # Check if seen before, if so you're in a loop
        if n in memo: 
            return False 
        # If not seen before, add it to the set
        else:
            memo.add(n)
    else:
        return True 





# num = 19
# print(isHappy(num))

for i in range(1, 100):
    print(isHappy(i))