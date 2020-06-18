class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = '+'
MINUS = '-'
TIMES = '*'
DIVIDE = '/'


def evaluate(root):
    result = 0
    if root.val in [PLUS, MINUS, TIMES, DIVIDE]:
        left = evaluate(root.left)
        right = evaluate(root.right)

        if root.val == PLUS:
            result = left + right
        elif root.val == MINUS:
            result = left - right
        elif root.val == TIMES:
            result = left * right
        elif root.val == DIVIDE:
            result = left / right

        return result

    return int(root.val)


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)

print(evaluate(tree))
# 45

root = Node('+')
root.left = Node('*')
root.left.left = Node('5')
root.left.right = Node('4')
root.right = Node('-')
root.right.left = Node('100')
root.right.right = Node('20')
print(evaluate(root))
# 100

root = Node('+')
root.left = Node('*')
root.left.left = Node('5')
root.left.right = Node('4')
root.right = Node('-')
root.right.left = Node('100')
root.right.right = Node('/')
root.right.right.left = Node('20')
root.right.right.right = Node('2')
print(evaluate(root))
# 110
