class Node:
    def __init__(self, data=None, next=None):
        # Value and pointer(to a Node)
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        """Insert node at beg of LL"""
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        # Traverse
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        """Insert node at end of LL"""
        # Insert at beginning if empty
        if self.head is None:
            self.head = Node(data, None)
            return

        # Iterate to the end and add Node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """Take list of values and make LL"""
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """Get length of LL"""
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def remove_at(self, index):
        """Remove element at given index"""
        if index < 0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        # Remove head, just move pointer to next
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
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
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

if __name__ == "__main__":
    ll = LinkedList()

    # Insert values
    ll.insert_at_beg(5)
    ll.print()
    ll.insert_at_beg(85)
    ll.print()
    ll.insert_at_end(98)
    ll.print()

    ll.insert_values(["mango", "grapes", "orange"])
    ll.print()
    print("Length:", ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(1, "figs")
    ll.print()
