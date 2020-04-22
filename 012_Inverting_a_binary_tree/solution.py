class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value, end=" ")
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()


def invert(node):
    if not node:
        return
    temp = node.left
    node.left = node.right
    node.right = temp

    invert(node.right)  # invert old left node
    invert(node.left)  # invert old right node

root = Node('a')
root.left = Node('b')
root.right = Node('c')

root.left.left = Node('d')
root.left.right = Node('e')

root.right.left = Node('f')

print('Initialize Binary Tree: ')
root.preorder()
print()

invert(root)
print('Revert Binary Tree: ')
root.preorder()
print()
