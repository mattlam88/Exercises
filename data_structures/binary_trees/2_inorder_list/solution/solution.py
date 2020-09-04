class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right

    
def Inorder(root):
    lst = []
    if root == None:
        return lst
    return Inorder(root.left) + [root.key] + Inorder(root.right)

