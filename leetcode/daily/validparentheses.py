# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


def isValid(s: str) -> bool: 
    #Use a stack, last in first out
    stack = []
    # valid sets of parens
    valid_parens = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    for paren in s:
        if paren in valid_parens: 
            stack.append(paren)
        else: 
            if len(stack) != 0 and paren == valid_parens[stack[-1]]:
                stack.pop()
            else: 
                return False 

    return len(stack) == 0



s = "()"
print(isValid(s))
print("------")
s = "()[]{}"
print(isValid(s))
print("------")
s = "(]"
print(isValid(s))
print("------")
s = "((([{}])))"
print(isValid(s))
print("------")