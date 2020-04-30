class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val, end=' ')
            c = c.next

        print()


class Solution():
    def intersection(self, a: Node, b: Node) -> Node:
        '''
        Move the pointer of long LinkedList to the position
        where two LinkedList have same length
        Traverse either of it
        :param a:
        :param b:
        :return:
        '''

        len1 = self.get_len(a)
        len2 = self.get_len(b)

        # Make sure a is longer LikedList
        if len2 > len1:
            a, b = b, a
            len1, len2 = len2, len1

        for _ in range(len1 - len2):
            a = a.next

        while a != b:
            a = a.next
            b = b.next

        return a

    def get_len(self, head: Node):
        length = 0
        while head:
            length += 1
            head = head.next

        return length

    def intersection_hashmap(self, a: Node, b: Node) -> Node:
        '''
        1. Traverse LinkedList a and store the address/reference
        to each node in a hash set.
        2. Then check LinkedList b: if node appears in hash set, then
        this node is the intersection node
        :param a:
        :param b:
        :return:
        '''

        counter = {}

        c = a
        while c:
            counter[c] = 1
            c = c.next

        print(counter.keys())
        c = b
        while c:
            if c not in counter:
                c = c.next
                continue

            return c

        return None


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

a.prettyPrint()
b.prettyPrint()
c = Solution().intersection_hashmap(a, b)
c.prettyPrint()
# 3 4