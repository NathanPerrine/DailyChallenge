# There are N block from 0 to N-1. A couple of frogs were sitting together on one block, They had a quarrel and need to jump away from one another. The frogs can only jump to another block if the height of the other block is greater than equal to the current one. You need to find the longest possible distance that they can possible create between each other, if they also choose to sit on an optimal starting block initially.

def greatest_distance(blocks):
    greatest = 0 

    if len(blocks) < 1: return greatest 

    for i in range(len(blocks)):
        f1, f2 = i, i
        n = i 

        while n > 0:
            if blocks[n] <= blocks[n-1]:
                f1 = n-1 
                n -= 1
            else: break 

        n = i 
        while n < len(blocks)-1:
            if blocks[n] <= blocks[n + 1]:
                f2 = n+1
                n += 1
            else: break
        
        greatest = max(greatest, f2 - f1 + 1)
    return greatest


b = [1, 2, 34, 5, 6, 8, 10, 22]
print(greatest_distance(b))