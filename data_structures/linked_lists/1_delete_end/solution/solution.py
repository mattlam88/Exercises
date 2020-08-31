class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self, head=None):
        self.head = head

    def delete_at_end(self):
        if self.head == None:
            return None
        x = self.head
        while x.next.next is not None:
            x = x.next
        x.next = None
