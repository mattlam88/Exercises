class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = None
    
    def insert_at_end(self, data):
        current_node = self.head
        prev_node = current_node
        while current_node != None:
            prev_node = current_node
            current_node = current_node.next
        new_node = Node(data)
        prev_node.next = new_node
        
