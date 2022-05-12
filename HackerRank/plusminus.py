

def plusMinus(arr):
    fullLength = len(arr)

    def findNeg(num):
        return True if num < 0 else False

    def findPos(num):
        return True if num > 0 else False

    def findZero(num):
        return True if num == 0 else False

    negs    = len(list(filter(findNeg, arr)))
    pos     = len(list(filter(findPos, arr)))
    zero    = len(list(filter(findZero, arr)))

    negDecimals  = round((negs / fullLength), 6)
    posDecimals  = round((pos / fullLength), 6)
    zeroDecimals = round((zero / fullLength), 6)

    print("{:.6f}".format(negDecimals))
    print("{:.6f}".format(posDecimals))
    print("{:.6f}".format(zeroDecimals))



l1 = [-2, -1, 0, 1, 2]
plusMinus(l1)
print("----")
l2 = [-4, 3, -9, 0, 4, 1]
plusMinus(l2)