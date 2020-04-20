class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += ' '
            node = node.next
        print(output)

    def reverseInteractively(self, head):
        # Fill in this
        previous = None
        current = head
        while current:
            tmp = current.next
            if current:
                current.next = previous
                previous = current
                current = tmp

    def reverseRecursively(self, head):
        # Fill in this
        previous = None
        self.reverseRecursively_(head, previous)

    def reverseRecursively_(self, current, previous):
        if current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp
            self.reverseRecursively_(current, previous)


testHead = ListNode(4)
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(1)
testTail = ListNode(0)

testHead.next = node1
node1.next = node2
node2.next = node3
node3.next = testTail

print('Inital list: ')
testHead.printList()
testHead.reverseInteractively(testHead)
# testHead.reverseRecursively(testHead)
print('List after reversal: ')
testTail.printList()
