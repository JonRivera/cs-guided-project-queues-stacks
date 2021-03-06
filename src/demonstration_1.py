"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.

You already have a `Stack` class that you've implemented using a dynamic array.

Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.

*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""


class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


# Understand:
# We are trying find the largest element for a given stack
# Implement a get_max() method that returns this element
# Plan
# Using 2 stack classes
# The first stack stores the elements
# The second stack keeps track of the biggest element
# If max_stack is empty then store the input inside this stack -> compare the current item to the one
# In Max stack -> if the current item is less than the one store in max stack pop the item in max stack
# and push the bigger
# Element back into this stack
class MaxStack:
    def __init__(self):
        # Your code here
        # Tracks max
        max_stack = Stack()
        stack

    def push(self, item):
        """Add a new item onto the top of our stack."""
        # Your code here

    def pop(self):
        """Remove and return the top item from our stack."""
        # Your code here

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here
