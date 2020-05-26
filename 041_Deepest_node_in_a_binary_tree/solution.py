class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    if not node:
        return

    levels = find_height(node)

    deepest_(node, levels)
    return levels


def deepest_(node, levels):
    if not node:
        return
    if levels == 1:
        print(node.val, end=" ")
    else:
        deepest_(node.left, levels - 1)
        deepest_(node.right, levels - 1)


def find_height(node):
    if not node:
        return 0

    leftHeight = find_height(node.left)
    rightHeight = find_height(node.right)

    return max(leftHeight, rightHeight) + 1


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')
root.right.right = Node('e')
root.right.right.right = Node('f')

print(deepest(root))
# (d, 3)