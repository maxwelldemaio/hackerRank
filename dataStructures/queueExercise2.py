# Python program to generate binary numbers from
# 1 to n

# This function uses queu data structure to print binary numbers
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)
        return

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


def generatePrintBinary(n):
    # Create an empty queue
    q = Queue()

    # Enqueu the first binary number
    q.enqueue("1")

    # This loop is like BFS of a tree with 1 as root
    # 0 as left child and 1 as right child and so on
    while(n > 0):
        n -= 1
        # Print the front of queue
        s1 = q.dequeue()
        print(s1)

        s2 = s1  # Store 2s1 before changing it

        # Append "0" to s1 and enqueue it
        q.enqueue(s1+"0")

        # Append "1" to s2 and enqueue it. Note that s2
        # contains the previous front
        q.enqueue(s2+"1")


# Driver program to test above function
n = 10
generatePrintBinary(n)
