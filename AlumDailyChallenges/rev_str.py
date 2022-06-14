def reverse_string(str):
    return str[::-1]

s = ["h","e","l","l","o"]
# print(reverse_string(s))

def reverse_string2(str):
    l = 0
    r = len(str)-1

    while l < r: 
        str[l], str[r] = str[r], str[l]
        l += 1 
        r -= 1 

    return str

s = ["h","e","l","l","o"]
print(reverse_string2(s))