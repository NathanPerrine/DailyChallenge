pick = 7
def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    elif num < pick:
        return 1

def guessNumber(n: int) -> int:
    lowest = 1
    highest = n
    while lowest <= highest:
        mid = (lowest + highest) // 2
        print(mid)
        myGuess = guess(num = mid)
        print(myGuess)
        
        if myGuess == 0:
            return mid
        elif myGuess == 1:
            lowest = mid + 1
        elif myGuess == -1:
            highest = mid - 1

print(guessNumber(6))