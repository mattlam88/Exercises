class Node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right


def Postorder(root):
    lst = []
    if not root:
        return lst
    return Postorder(root.left) + Postorder(root.right) + [root.key]

