class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        # preOrder traversal
        answer = str(self.key) + ' '
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)

        return answer

INT_MIN = -2147483648
INT_MAX = 2147483648


def largest_bst_subtree(root):
    result = largest_bst(root)
    return result[3]


def largest_bst(root):
    if not root:
        return 0, INT_MIN, INT_MAX, 0, True

    if not root.left and not root.right:
        return 1, root.key, root.key, 1, True

    left = largest_bst(root.left)
    right = largest_bst(root.right)

    result = [0, 0, 0, 0, 0]  # level, min, max, returnTreeNode, flag
    result[0] = 1 + left[0] + right[0]

    # if whole tree is BST
    if left[4] and right[4] and left[1] < root.key < right[2]:
        result[2] = min(left[2], min(right[2], root.key))
        result[1] = max(right[1], max(left[1], root.key))

        result[3] = root
        result[4] = True

        return result

    # if whole tree is not BST, return maximum of left and right subtree
    # print(left)
    # print(right)
    if isinstance(left[3], TreeNode) and isinstance(right[3], TreeNode):
        result[3] = left[3] if left[1] > right[1] else right[3]
    elif isinstance(left[3], TreeNode):
        result[3] = left[3]
    elif isinstance(right[3], TreeNode):
        result[3] = right[3]


    result[4] = False

    return result


node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)

print(largest_bst_subtree(node))
# 7 4 9

n = TreeNode(5)
n.left = TreeNode(2)
n.right = TreeNode(4)
n.left.left = TreeNode(1)
n.left.right = TreeNode(3)

print(largest_bst_subtree(n))
# 2 1 3

n = TreeNode(50)
n.left = TreeNode(30)
n.left.left = TreeNode(5)
n.left.right = TreeNode(20)
n.right = TreeNode(60)
n.right.left = TreeNode(45)
n.right.right = TreeNode(70)
n.right.right.left = TreeNode(65)
n.right.right.right = TreeNode(80)

print(largest_bst_subtree(n))
# 60 45 70 65 80