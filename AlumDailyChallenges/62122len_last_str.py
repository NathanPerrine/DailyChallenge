# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# If you want to make this more challenging, solve it in O(n) Time and O(1) Space.
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

import timeit

def find_last_len(s: str) -> int: 
    return len(s.strip().split()[-1])

def find_last_nostrip(s:str) -> int: 
    count = 0
    i = len(s)-1 
    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
            continue 
        while i >= 0 and s[i] != ' ':
            count += 1 
            i -= 1
        return count




words = "Hello World"
print(find_last_len(words))
words = "   fly me   to   the moon  "
print(find_last_len(words))
words = "luffy is still joyboy"
print(find_last_len(words))
print("-------------------")
words = "Hello World"
print(find_last_nostrip(words))
words = "   fly me   to   the moon  "
print(find_last_nostrip(words))
words = "luffy is still joyboy"
print(find_last_nostrip(words))
print("-------------------")

words_strip = timeit.timeit(lambda: find_last_len("   fly me   to   the moon  "), number=1_000_000)
words_no_strip = timeit.timeit(lambda: find_last_nostrip("   fly me   to   the moon  "), number=1_000_000)

print(f'{words_strip=}')
print(f'{words_no_strip=}')