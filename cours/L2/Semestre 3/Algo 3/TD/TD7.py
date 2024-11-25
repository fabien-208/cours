class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_maximum(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val


def cherche(node, value):
    current = node
    if current.val == value:
        return True
    else:
        if current.val < value and current.left != None:
            cherche(current.left)
        if current.val > value and current.right != None:
            cherche(current.right)
    return False