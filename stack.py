from referential_array import build_array


class Stack:
    def __init__(self, size):
        self.array = build_array(size)
        self.count = 0
        self.top = -1

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.array)

    def size(self):
        return self.count

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item
            self.count += 1
            return True
        return False

    def pop(self):
        assert self.count > 0, 'no items'
        item = self.array[self.top]
        self.top -= 1
        self.count -= 1
        return item


def check_parentheses(string):
    n = Stack(20)
    count = 0
    for i in string:
        if i == "(":
            count += 1
        n.push(i)
    while not n.is_empty():
        item = n.pop()
        if item == ")":
            count -= 1

    if count == 0:
        print('balanced')
    else:
        print('not balanced')


check_parentheses('(buirvwwwie)')


def partition(alist, start, end):
    mid = (start + end) // 2
    pivot = alist[mid]
    alist[mid], alist[start] = alist[start], m
    index = start
    for i in range(index + 1, end):
        if alist[i] < pivot:
            index += 1
            swap(index, i)
    swap(index, start)
    return index
