class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):

    ceil = findCeil(root_node, k)
    floor = findFloor(root_node, k)

    return floor, ceil


def insert(root_node, value):
    if not root_node:
        return Node(value)

    if value < root_node.value:
        root_node.left = insert(root_node.left, value)
    else:
        root_node.right = insert(root_node.right, value)

    return root_node


def findCeil(root_node, k):
    if not root_node:
        return None

    # if node.value is equal to k
    if root_node.value == k:
        return root_node.value

    # if node.value is smaller then k is on the right
    if root_node.value < k:
        return findCeil(root_node.right, k)

    # else node.value is greater then k is on the left
    val = findCeil(root_node.left, k)
    if val and val >= k:
        return val
    else:
        return root_node.value


def findFloor(root_node, k):
    if not root_node:
        return None

    if root_node.value == k:
        return root_node.value

    # if node.value is greater then k is on the left
    if root_node.value > k:
        return findFloor(root_node.left, k)

    # else node.value is smaller then k is on the right
    val = findFloor(root_node.right, k)
    if val and val <= k:
        return val
    else:
        return root_node.value

# root = Node(8)
# root.left = Node(4)
# root.right = Node(12)
#
# root.left.left = Node(2)
# root.left.right = Node(6)
#
# root.right.left = Node(10)
# root.right.right = Node(14)

root = insert(None, 8)
for item in [4, 12, 2, 6, 10, 14]:
    insert(root, item)

print(findCeilingFloor(root, 5))

for i in range(16):
    print('{0}: {1}'.format(i, findCeilingFloor(root, i)))
