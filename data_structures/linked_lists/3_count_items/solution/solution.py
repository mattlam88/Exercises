#write your answers here
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def get_count(self):
        current_node = self.head
        count = 0
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count