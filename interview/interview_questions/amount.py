# You decide to create a substitution cipher. The cipher alphabet is based on a key shared amongst those of your friends who don't mind spoilers.

# Suppose the key is:
# "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!". 

# We use only the unique letters in this key to set the order of the characters in the substitution table.

# T H E Q U I C K O N Y X G B L R A S W D J M P V Z F

# (spaces added for readability)

# We then align it with the regular alphabet:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# T H E Q U I C K O N Y X G B L R A S W D J M P V Z F

# Which gives us the substitution mapping: A becomes T, B becomes H, C becomes E, etc.

# Write a function that takes a key and a string and encrypts the string with the key.

# Example:
# key = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!"
# encrypt("It was all a dream.", key) -> "Od ptw txx t qsutg."
# encrypt("Would you kindly?", key) -> "Pljxq zlj yobqxz?"

# Complexity analysis:

# m: The length of the message
# k: The length of the key

key1 = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!"
message = "It was all a dream."
message2 = "Would you kindly?"

def encrypt(message, key):
    new_key = []
    out = ""
    for v in key:
        if v.upper() not in new_key and v.isalpha():
            new_key.append(v.upper())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_key = "".join(new_key)
    
    for letter in message:
        if letter.isalpha():
            if letter.upper() == letter:
                out += new_key[alphabet.index(letter.upper())]
            else:
                out += new_key[alphabet.index(letter.upper())].lower()
        else:
            out += letter
    return out

print(encrypt(message, key1))
print("Od ptw txx t qsutg.")

print(encrypt(message2, key1))
print("Pljxq zlj yobqxz?")








# message1 = "One does not simply walk into Mordor"
# rows1, cols1 = 6, 6

# message2 = "1.21 gigawatts!"
# rows2, cols2 = 5, 3
# rows3, cols3 = 3, 5

# def transpose(message, rows, cols):
#     out = ""

#     # out += message[0]
#     # print(len(message))
#     i = 0
#     starter = 1
#     while len(out) < len(message):
#         # print(i)
#         out += message[i]
#         i += cols 

#         if i > len(message) -1:
#             i = starter
#             starter += 1

#     return out

# print(transpose(message1, rows1, cols1))
# print("Oe y Mnss ioe iwnr nmatddoploootlk r")
# # print(message1[35])

# print(transpose(message2, rows2, cols2))
# print("11iwt. gas2gat!")
# print(transpose(message2, rows3, cols3))
# print("1ga.it2gt1as w!")