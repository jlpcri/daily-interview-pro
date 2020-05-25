from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value) + ' '
            nodes.append(node.left)
            nodes.append(node.right)

        return answer


def createBalancedBST(nums):
    '''
    1. Get the middle of the array and make it as root
    2. Recursively do same for left half and right half
        a. Get the middle of left half and make it as left child of root
        b. Get the middle of right half and make it as right child of root
    '''
    if not nums:
        return None

    # find the middle element of nums
    middle_idx = len(nums) // 2

    # make the middle element as root
    root = Node(nums[middle_idx])

    # left subtree of root
    root.left = createBalancedBST(nums[:middle_idx])

    # right subtree of root
    root.right = createBalancedBST(nums[middle_idx + 1:])

    return root


nums = [1, 2, 3, 4, 5, 6, 7]
print(createBalancedBST(nums))
#4261357