# Find the longest uniform substring of a given string.

# def longestsub(astring: str) -> str:
#     l, r = 0, 1
#     longest = 0
#     start = 0

#     if len(astring) == 0:
#         return -1
#     if len(astring) == 1:
#         return (0, 1)

#     while r < len(astring):
#         # a == a, found a uniform substring
#         if astring[l] == astring[r]:
#             r += 1
#         # a == b, substring doesn't exist or ended
#         else:
#             if r-l > longest:
#                 longest = r-l 
#                 start = l
#             l = r
#             r += 1
    
#     # for checking if the last part of the string is the longest uniform substring 
#     if r-l > longest:
#         longest = r-l 
#         start = l

#     return (start, longest)


# sentence = "abbbccdefg"
# print(longestsub(sentence))
# sentence = ""
# print(longestsub(sentence))
# sentence = "ag"
# print(longestsub(sentence))
# sentence = "abbbccdefggggggggg"
# print(longestsub(sentence))



def longest_sub2(s):
    # Two pointers to move through the string
    l, r = 0, 1
    longest, start = 0, 0 
    size = len(s)

    # Test if the string is too small
    if size == 0:
        return -1
    if size == 1:
        return (0, 1)

    # Loop through the string until the right pointer is at the end 
    while r < size:
        # Check to see if you've found a uniform substring
        if s[l] == s[r]:
            # uniform substring found, move right pointer
            r += 1
        # Check if substring not found OR at the end of the string
        if r == size or s[l] != s[r]:
            # Find the longest sub 
            if longest < r-l:
                longest = r-l
                start = l 
            # Move pointers, l can jump to the right pointer, right can increment by 1 
            l = r
            r += 1
    
    return (start, longest)

sentence = "abbbccdefg"
print(longest_sub2(sentence))
sentence = ""
print(longest_sub2(sentence))
sentence = "ag"
print(longest_sub2(sentence))
sentence = "abbbccdefggggggggg"
print(longest_sub2(sentence))
sentence = "dabbbccddddddddddddefgggg453215iiii"
print(longest_sub2(sentence))
