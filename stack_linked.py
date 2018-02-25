from Node import Node


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        assert not self.is_empty(), 'stack empty'
        item = self.top.item
        self.top = self.top.next
        return item


if __name__ == '__main__':
    t = Stack()
    t.push('me')
    t.push('k')
    print(t.pop())
    print(t.pop())

