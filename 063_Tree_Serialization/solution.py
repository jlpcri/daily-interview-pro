from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # preorder traversal
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)

        if self.right:
            result += str(self.right)

        return result


MARKER = '# '


def serialize(root):
    result = ''
    if root:
        result += str(root.val) + ' '
        if root.left:
            result += serialize(root.left)
        else:
            result += MARKER

        if root.right:
            result += serialize(root.right)
        else:
            result += MARKER

    return result


def deserialize(data):
    if not data:
        return None

    vals = data.split(' ')
    queue = deque(vals)

    return deserialize_helper(queue)


def deserialize_helper(q):
    element = q.popleft()
    if element == MARKER.strip():
        return None

    root = Node(element)
    root.left = deserialize_helper(q)
    root.right = deserialize_helper(q)

    return root


tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #

print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 1 3 2 5 4 7
