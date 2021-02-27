from collections import deque
import threading
import time


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

# Create our order stream
food_order_queue = Queue()

def serve_orders():
    """Fufill customer orders"""
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving:", order)
        time.sleep(2)

def place_orders(orders):
    """Place orders for kitchen staff to serve"""
    for order in orders:
        print("Placing order for:", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


if __name__ == "__main__":
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()
