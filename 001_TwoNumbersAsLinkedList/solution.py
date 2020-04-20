class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in
        '''
        Special cases:
        1. l1 and l2 could have different number of digits
        2. the sum could have an extra digit
        '''

        head = result = ListNode(0)

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            digitSum = val1 + val2 + c
            c = 1 if digitSum >= 10 else 0
            digitSum %= 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            result.val = digitSum
            result.next = ListNode(c) if l1 or l2 or c else None
            result = result.next
        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(7)
l2.next = ListNode(0)
l2.next.next = ListNode(8)
l2.next.next.next = ListNode(2)


result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next

print()
