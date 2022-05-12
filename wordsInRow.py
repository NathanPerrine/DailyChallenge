# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:
# Input: words = ["omk"]
# Output: []
# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

def inRow(words):
    rowOne = set("qwertyuiop")
    rowTwo = set("asdfghjkl")
    rowThree = set("zxcvbnm")
    output = []
    for word in words:
        wordSet = set(word.lower())

        if len(wordSet - rowOne) == 0:
            output.append(word)
        elif len(wordSet - rowTwo) == 0:
            output.append(word)
        elif len(wordSet - rowThree) == 0:
            output.append(word)

    return output



words = ["Hello","Alaska","Dad","Peace"]
print(inRow(words))
words = ["omk"]
print(inRow(words))
words = ["adsdf","sfd"]
print(inRow(words))