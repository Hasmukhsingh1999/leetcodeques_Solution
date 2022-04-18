'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.'''

def isValid(str):
    stack = []
    for char in str:
        if char == ')' or char == ']' or char == '}':
            stack.append(stack)
        elif not stack:
            stack.pop()

        elif char == '(' and stack[-1]=='(':
            stack.pop()
        elif char =='[' and stack[-1]=='[':
            stack.pop()
        elif char =='{' and stack[-1]=='{':
            stack.pop()
        else:
            return False
    return len(stack)

str = input()
print(isValid(str))
