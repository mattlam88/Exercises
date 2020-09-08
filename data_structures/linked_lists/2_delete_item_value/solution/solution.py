class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self,head=None):
        self.head = head

    def delete_item_by_value(self, x):
        current_node = self.head
        prev_node = current_node

        while current_node != None and current_node.data != x:
            prev_node = current_node
            current_node = current_node.next

        if current_node != None:
            prev_node.next = current_node.next