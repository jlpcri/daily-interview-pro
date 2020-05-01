class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def prettyPrint(self):
        current = self
        while current:
            print(current.value, end=' ')
            current = current.next

        print()


def removeConsecutiveSumTo0(head: Node) -> Node:
    # Fill this in.
    # define a dummy node always point to head
    dummy = Node(0)
    dummy.next = head

    # keep a dict of cumulative sums and nodes accordingly
    # cumulative sum of dummy node is 0
    sum_dict = {}

    # sum before current node
    previous_sum = 0
    sum_dict[previous_sum] = dummy

    while head:
        previous_sum += head.value

        '''
        Traverse through the linked list while computing a cumulative sum.
        At each node, save the sum and the associated node to the sums
        dictionary. When a sum is repeated, a zero sum has been found.
        Execute the following steps:
        * Modify a pointer to bypass the nodes in the zero sum.
        * Step through each node in the zero sum and remove its entry
          from the sums dictionary.
        * From the current node, which the last node in the zero sum, move
          on to the next node and continue.
        '''
        if previous_sum in sum_dict:
            # remove entries which sum = 0 from sum_dict
            remove_node = sum_dict[previous_sum].next
            tmp_sum = previous_sum
            while remove_node != head:
                tmp_sum += remove_node.value
                sum_dict.pop(tmp_sum, None)
                remove_node = remove_node.next

            # draw a link to skip deleted nodes
            sum_dict[previous_sum].next = head.next

        else:
            # add current node to sum_dict
            sum_dict[previous_sum] = head

        head = head.next

    return dummy.next

# node = Node(10)
# node.next = Node(5)
# node.next.next = Node(-3)
# node.next.next.next = Node(-3)
# node.next.next.next.next = Node(1)
# node.next.next.next.next.next = Node(4)
# node.next.next.next.next.next.next = Node(-4)
# node.prettyPrint()
#
# node = removeConsecutiveSumTo0(node)
# node.prettyPrint()
# 10

list_ = [
    [10, 5, -3, -3, 1, 4, -4],    # return 10
    [1, 2, -3, 3, 1],             # [3, 1]
    [1, 2, 3, -3, 4],             # [1, 2, 4]
    [1, 2, 3, -3, -2]             # [1]
]

for item in list_:
    for idx, val in enumerate(item):
        if idx == 0:
            node = Node(val)
            head = node
        else:
            node.next = Node(val)
            node = node.next

    head.prettyPrint()
    head = removeConsecutiveSumTo0(head)
    head.prettyPrint()