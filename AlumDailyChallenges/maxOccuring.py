def getMaxChar(text):
    freq = {}
    for char in text: 
        freq[char] = freq.get(char, 0) + 1
    max_char = ""
    max_freq = 0
    for item in freq:
        if freq[item] > max_freq:
            max_freq = freq[item]
            max_char = item
    return max_char


test = "aabbbaccc"
print(getMaxChar(test))