# https://medium.com/@RamkrishnaKulka/traversal-of-a-self-looping-tree-a2e985eb9b34

class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(root):
    if root.left == root and root.right == root:
        return True
    if root.left != root and root.left.right == root:
        return True
    if root.right != root and root.right.left == root:
        return True
    return False


def inorder(root: Node):
    if is_leaf(root):
        print(root.val)
        return
    if root.left != root:
        inorder(root.left)
    print(root.val)
    if root.right != root:
        inorder(root.right)


n1 = Node(1)
n2 = Node(5)
n3 = Node(7)
n1.left = n1
n1.right = n2
n2.left = n1
n2.right = n3
n3.left = n2
n3.right = n3
n4 = Node(2)
n5 = Node(4)
n6 = Node(8)
n4.left = n1
n4.right = n4
n5.left = n5
n5.right = n2
n6.left = n3
n6.right = n6
n7 = Node(3)
n7.left = n4
n7.right = n5
root = Node(6)
root.left = n7
root.right = n6
inorder(root)
