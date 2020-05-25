class Queue:
    def __init__(self):
        # Fill this in.
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        # Fill this in.
        self.s1.append(val)

    def dequeue(self):
        # Fill this in.
        if len(self.s1) == 0 and len(self.s2) == 0:
            return "Queue is empty"

        # Move elements from stack1 to stack2 only if stack2 is empty
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                tmp = self.s1[len(self.s1) - 1]
                self.s1.pop()
                self.s2.append(tmp)
        tmp = self.s2[len(self.s2) - 1]
        self.s2.pop()

        return tmp


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3