class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        """Insert node at beg of LL"""
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def get_last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        # Traverse
        while itr:
            llstr += str(itr.data) + '<--->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        iter = self.get_last()
        print(iter)
        llstr = str(iter.data) + '--->' 
        while iter.prev:
            llstr += str(iter.prev.data) + '<--->'
            iter = iter.prev
        print(llstr)


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beg("figs")
    dll.insert_at_beg("mango")
    dll.insert_at_beg("grapes")
    dll.print_forward()
    dll.print_backward()
