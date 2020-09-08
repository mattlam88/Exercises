class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_after_item(self, x, data):
        current_node = self.head
        prev_node = self.head

        if current_node == None:
            new_node = Node(data)
            self.head = new_node
            return

        while not current_node == None and not current_node.data == x:
            prev_node = current_node
            current_node = current_node.next
        new_node = Node(data)
        if current_node == None:
            prev_node.next = new_node
        else:
            new_next = current_node.next
            current_node.next = new_node
            new_node.next = new_next
    # def insert_after_item(self, x, data):
    #     cur_node = self.head
    #     prev_node = self.head
    #     if cur_node == None:
    #         new_node = Node(data)
    #         self.head = new_node
    #         return
    #     while(not cur_node == None and cur_node.data != x):
    #         prev_node = cur_node
    #         cur_node = cur_node.next
    #     new_node = Node(data)
    #     if cur_node == None:
    #         prev_node.next = new_node
    #     else:
    #         new_next = cur_node.next
    #         cur_node.next = new_node
    #         new_node.next = new_next
   

        
