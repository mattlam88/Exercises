class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

left_leaf = Node(4,None,None)
right_leaf = Node(7,None,None)
sample_tree = Node(5,left_leaf,right_leaf)



