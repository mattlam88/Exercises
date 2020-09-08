class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self,head=None):
        self.head = head
    
    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
