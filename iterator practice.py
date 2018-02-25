class OddIterator:
    def __init__(self, n, end):
        self.current = n
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        while self.current % 2 != 1:
            self.current += 1

        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


class NegativeIteraor:
    def __init__(self, alist):
        self.list = alist
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.list):
            raise StopIteration
        while self.current < len(self.list) and self.list[self.current] >= 0:
            self.current += 1
        if self.current >= len(self.list):
            raise StopIteration
        item = self.list[self.current]
        self.current += 1
        return item


t = NegativeIteraor([2, 3, 2, 4, 2, -3,-2])
for item in t:
    print(item)

# n = OddIterator(12, 19)
# for val in n:
#     print(val)
