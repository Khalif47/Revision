from referential_array import build_array


class heap:
    def __init__(self):
        self.count = 0
        self.array = build_array(100)

    def add(self, key, value):
        item = (key, value)
        self.array[self.count + 1] = item
        self.count += 1
        self.rise(self.count)

    def rise(self, k):
        while k > 1 and self.array[k] > self.array[k // 2]:
            self.array[k], self.array[k // 2] = self.array[k // 2], self.array[k]
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.count:
            child = self.largest(k)
            if self.array[child] < self.array[k]:
                break
            self.array[child], self.array[k] = self.array[k], self.array[child]
            k = child

    def largest(self, k):
        if 2 * k == self.count or self.array[2 * k] > self.array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def __str__(self):


    def heap_sort(self, alist):
        for i in range(alist):
            self.add(alist[i])
        return self

def insert(self, item):
    if empry:
        self[0]  = item
    if not self.is_full():
        n = len(self)
        i = n -1 # back of list
        while i >= 0 and self.array[i] > item:
            alist[k + 1] = [k]
        alist[k + 1] = item
        self.coimt += 1


def rehash():
    new = build_array(ts * 2)
    for i in range(self.tablesize):
        if self.array[i] is not None:


