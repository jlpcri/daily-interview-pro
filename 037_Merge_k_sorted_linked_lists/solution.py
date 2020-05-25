import heapq


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ''
        while c:
            if c.val == 0:
                answer += '0 '
            else:
                answer += (str(c.val) + ' ') if c.val else ''
            c = c.next

        return answer


def merge(lists):
    '''
    Heapq is the data structure mainly used to represent a priority queue
    :param lists:
    :return:
    '''
    heap = []

    for each_list in lists:
        while each_list:
            heapq.heappush(heap, each_list.val)
            each_list = each_list.next

    dummy = head = Node(-1)

    for i in range(len(heap)):
        dummy.next = Node(heapq.heappop(heap))
        dummy = dummy.next

    return head.next


a = Node(1, Node(3, Node(5, Node(7))))
b = Node(2, Node(4, Node(6, Node(8))))
c = Node(0, Node(9, Node(10, Node(11))))

print(a)
print(b)
print(c)
print(merge([a, b, c]))