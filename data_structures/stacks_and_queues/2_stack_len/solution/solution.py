class ListNode:
  def __init__(self, value):
      self.value = value
      self.next = None

class Stack:
    def __init__(self):
        self.head_node = None

    def push(self, value):
        new_head = ListNode(value)
        new_head.next = self.head_node
        self.head_node = new_head

    def pop(self):
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.next
            return value
        else:
            raise IndexError

    # Fill in the code for __len__
    def __len__(self):
        head_node = self.head_node
        num_nodes = 0
        if head_node == None:
            return 0
        while head_node:
            num_nodes += 1
            head_node = head_node.next
        return num_nodes