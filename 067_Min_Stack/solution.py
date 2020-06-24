class minStack(object):
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if len(self.min) > 0:
            if x <= self.min[len(self.min) - 1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self):
        top_min = self.min[-1]
        top_stack = self.stack[-1]

        if top_min == top_stack:
            self.min = self.min[:-1]
            self.stack = self.stack[:-1]
        else:
            self.stack = self.stack[:-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]


x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2

x = minStack()
x.push(3)
x.push(5)
print(x.getMin())
# 3
x.push(2)
x.push(1)
print(x.getMin())
# 1
x.pop()
print(x.getMin())
# 2
x.pop()
print(x.getMin())
# 3