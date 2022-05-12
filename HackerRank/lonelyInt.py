def lonelyinteger(a):
    lonely = {}
    for num in a:
        lonely[num] = lonely.get(num, 0) + 1
    lonely = [key for key, v in lonely.items() if v == 1]
    print(lonely)


l1 = [1,2,3,4,3,2,1]
lonelyinteger(l1)