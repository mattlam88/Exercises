class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right
    

def search(root, key):
    if not root:
        return False
    if key == root.key:
        return True
    elif key < root.key:
        return search(root.left, key)
    elif key > root.key:
        return search(root.right, key)
    
items = Node(6)
items.left = Node(4)
items.right = Node(9)
items.left.left = Node(3)
items.left.right = Node(5)
items.right.left = Node(7)
items.right.right = Node(11)

print(search(items,11)) 
print(search(items,8)) 
