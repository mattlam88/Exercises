class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def search(self, x):
        current_node = self.head
        while not current_node == None:
            if current_node.data == x:
                return True
            current_node = current_node.next
        return False
