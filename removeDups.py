def removeDups(s: str, k: int) -> str:
    stack = [] # [char, count]

    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1 
        else: 
            stack.append([c, 1])

        if stack[-1][1] == k:
            stack.pop()
        print(stack)

    res = ""
    for char, count in stack: 
        res += (char * count)
    return res

s = 'aabbbacc'
k = 3
print(removeDups(s, k))