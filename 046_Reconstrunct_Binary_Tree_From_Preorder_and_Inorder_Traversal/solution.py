from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val + ' '
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    build_tree.preorder_idx = 0
    root = build_tree(preorder, inorder, 0, len(inorder) - 1)

    print(root)


def build_tree(preorder, inorder, inorder_idx_start, inorder_idx_end):
    '''
    Recursive function to construct binary of size len from InOrder traversal and PreOrder traversal
    :param inorder: InOrder traversal list
    :param preorder: PreOrder traversal list
    :param inorder_idx_start:
    :param inorder_idx_end:
    :return:
    '''
    if inorder_idx_start > inorder_idx_end:
        return None

    tmp_node = Node(preorder[build_tree.preorder_idx])
    build_tree.preorder_idx += 1

    if inorder_idx_start == inorder_idx_end:
        return tmp_node

    inorder_idx = search(inorder, inorder_idx_start, inorder_idx_end, tmp_node.val)

    tmp_node.left = build_tree(preorder, inorder, inorder_idx_start, inorder_idx - 1)
    tmp_node.right = build_tree(preorder, inorder, inorder_idx + 1, inorder_idx_end)

    return tmp_node


def search(arr, start, end, val):
    '''
    Find index of value in arr
    :param arr:
    :param start:
    :param end:
    :param val:
    :return:
    '''
    for i in range(start, end + 1):
        if arr[i] == val:
            return i


# preOrder: root, left, right
l_p = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
# inOrder: left, root, right
l_i = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
# postOrder: left, right, root

tree = reconstruct(l_p, l_i)
# abcdefg