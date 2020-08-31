class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_after_item(self, x, data):
        if self.head == None:
            return None
        n = self.head

        
