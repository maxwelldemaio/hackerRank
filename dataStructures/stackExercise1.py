from collections import deque

# We can already use deque as a Stack


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# A stack based function to reverse a string


def reverse(string):
    n = len(string)

    # Create a empty stack
    stack = Stack()

    # Push all characters of string to stack
    for i in range(0, n, 1):
        stack.push(string[i])

    # Making the string empty since all
    #characters are saved in stack
    string = ""

    # Pop all characters of string and
    # put them back to string
    for i in range(0, n, 1):
        string += stack.pop()

    return string


print(reverse("checkcheck"))
