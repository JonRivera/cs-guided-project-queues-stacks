"""PROBLEM#1 - Use 2 Stacks to implement a Queue"""


# Recovery
#
# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Implement a queue using two stacks.
#
# You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the
# results of each "pop" operation that is performed.
# ````````````````````````````
# Example
#
# For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
# queueOnStacks(requests) = [1, 2].
#
# After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, "pop", and
# add the first element of the queue 1 to the answer array. The queue becomes {2}. After the fourth request, the
# queue is {2, 3}. Then we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        right.push(left.items[0])  # [5] # push the first element in the first stack fifo approach
        left.items = left.items[1:]  # at the sam etime remove that first element from stack1 by sliccing
        return right.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans


"""PROBLEM - DETERMINE IF THE BRACKET SEQUENCE IS A VALID SEQUENCE"""
"""
:type s: str
:rtype: bool
"""


def validBracketSequence(sequence):
    left = ['(', '{', '[']
    right = [')', '}', ']']
    stack = []
    for letter in sequence:
        if letter in left:
            stack.append(letter)
        elif letter in right:
            if len(stack) <= 0:
                return False
            if left.index(stack.pop()) != right.index(letter):
                return False
    return len(stack) == 0


# STACK SOLUTION
def validBracketSequence(sequence):
    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in sequence:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'  # last element to go in the stack will be what comes out

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack
