#Task: Implement a Python function to reverse a string using a stack data structure. Explain how a stack is used in this case and analyze the tim complexity of your implementation.


def reverse_string_using_stack(s):
    stack = []  # initialize an empty stack

    # push all characters of the string onto the stack
    for char in s:
        stack.append(char)

    reversed_string = ''
    # pop all characters from the stack to reverse the string
    while stack:
        reversed_string = reversed_string + stack.pop()

    return reversed_string

### Explanation of Stack Usage: 

## Pushing Characters:

# We iterate through each character of the input string and push it onto the stack. Since a stack follows the Last In First Out (LIFO) principle, the last character pushed onto the stack will be the first one to be popped off.

## Popping Characters:

# After all characters have been pushed onto the stack, we initialize an empty string (reversed_string). We then pop characters from the stack one by one and append them to reversed_string. This process effectively reverses the original string because the last character added to the stack (the last character of the original string) is the first one to be removed.
    
##Time Complexity Analysis:

#Time Complexity: The time complexity of this implementation is O(n), where n is the length of the input string. This is because we perform a single pass to push all characters onto the stack and another pass to pop all characters off the stack.

#Space Complexity: The space complexity is also O(n), as we are using a stack to store all the characters of the string.