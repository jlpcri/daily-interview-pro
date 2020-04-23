# Class to make a LinkedList Node which constructs stack
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class MaxStack():
    def __init__(self):
        self.top = None        # top node
        self.count = 0         # number of nodes in stack
        self.maximum = None    # maximum value of stack

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next

        out = '\n'.join(out)
        return 'Top {} \n\nStack: \n'.format(not self, out)

    __repr__ = __str__

    def max(self):
        if not self.top:
            return "Stack is Empty"
        else:
            print("Maximum Element in the stack is : {}".format(self.maximum))

    def isEmpty(self):
        if not self.top:
            return True
        else:
            return False

    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count

    # This method returns top of stack
    def peek(self):
        if not self.top:
            print("Stack is Empty")
        else:
            if self.top.value > self.maximum:    # current value = 2*x - maximum which x is pushed value
                print("Top Most Element is: {}".format(self.maximum))
            else:
                print("Top Most Element is: {}".format(self.top.value))

    # This method adds node to stack
    def push(self, value):
        if not self.top:
            self.top = Node(value)
            self.maximum = value
        elif value > self.maximum:
            temp = 2 * value - self.maximum  # variation of pushed value
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.maximum = value
            print("Insert variation value: {}".format(temp))
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

        print("Number Inserted: {}".format(value))


    # This method pops top of stack
    def pop(self):
        if not self.top:
            print("Stack is Empty")
        else:
            remove_node = self.top
            self.top = self.top.next
            if remove_node.value > self.maximum:    # need update maximum
                print("Remove variation value: {}".format(remove_node.value))
                print("Top Most Element Removed: {}".format(self.maximum))
                self.maximum = 2 * self.maximum - remove_node.value
            else:
                print("Top Most Element Removed: {}".format(remove_node.value))


# stack = MaxStack()
#
# stack.push(3)
# stack.push(5)
# stack.max()
# stack.push(7)
# stack.push(19)
# stack.max()
# stack.pop()
# stack.max()
# stack.pop()
# stack.peek()

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2