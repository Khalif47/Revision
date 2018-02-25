class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def is_empty(self):
        return self.front is None

    def push(self, item):
        self.rear.next = Node(item)
        self.rear = self.rear.next
