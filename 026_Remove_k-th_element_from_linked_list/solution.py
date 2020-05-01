class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


class Solution():
    def remove_kth_from_linked_list(self, head: Node, k: int) -> Node:
        '''
        The above algorithm could be optimized to one pass. Instead of one pointer,
        we could use two pointers. The first pointer advances the list by n+1 steps from the beginning,
        while the second pointer starts from the beginning of the list.
        Now, both pointers are exactly separated by nn nodes apart.
        We maintain this constant gap by advancing both pointers together
        until the first pointer arrives past the last node.
        The second pointer will be pointing at the nth node counting from the last.
        We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.
        :param head:
        :param k:
        :return:
        '''
        # define dummy node which is 0th node
        dummy = Node(0)

        dummy.next = head
        first_pointer = dummy
        second_pointer = dummy

        for _ in range(k + 1):
            first_pointer = first_pointer.next

        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        second_pointer.next = second_pointer.next.next

        return dummy.next


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]


head = Solution().remove_kth_from_linked_list(head, 5)
print(head)
# [1, 2, 4, 5]