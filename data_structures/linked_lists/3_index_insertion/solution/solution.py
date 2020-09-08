class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_index(self,index,data):
        current_node = self.head
        prev_node = current_node
        current_index = 1
        new_node = Node(data)

        while current_index < index:
            prev_node = current_node
            current_node = current_node.next
            current_index += 1
        prev_node.next = new_node
        new_node.next = current_node



