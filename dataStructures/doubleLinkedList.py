class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_last(self):
        """Get last node of DLL"""
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_beg(self, data):
        """Insert node at beg of DLL"""
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        """Insert node at end of DLL"""
        # Insert at beginning if empty
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        # Iterate to the end and add Node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None, itr)

    def get_length(self):
        """Get length of DLL"""
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def print_forward(self):
        """Print DLL in forward direction"""
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
        """Print DLL in reverse direction"""
        iter = self.get_last()
        llstr = str(iter.data) + '--->' 
        while iter.prev:
            llstr += str(iter.prev.data) + '<--->'
            iter = iter.prev
        print(llstr)

    def insert_values(self, data_list):
        """Take list of values and make DLL"""
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        """Remove element at given index"""
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        # Remove head, just move pointer to next
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        """Insert node at given index"""
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beg(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                node.next.prev = node
                node.prev.next = node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        """Insert data after data criteria encountered"""
        count = 0
        iter = self.head
        while iter:
            if iter.data == data_after:
                self.insert_at(count + 1, data_to_insert)
            count += 1
            iter = iter.next

    def remove_by_value(self, data):
        """Remove first node that contains data"""
        count = 0
        iter = self.head
        while iter:
            if iter.data == data:
                self.remove_at(count)
            count += 1
            iter = iter.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_values(["banana", "mango", "grapes", "orange"])
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_end("figs")
    dll.print_forward()
    dll.insert_at(0, "jackfruit")
    dll.print_forward()
    dll.print_forward()
    dll.insert_at(2, "kiwi")
    dll.print_forward()
