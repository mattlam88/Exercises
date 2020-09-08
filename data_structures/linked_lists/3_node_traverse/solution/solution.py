class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
            