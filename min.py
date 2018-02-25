class Prime:
    def __init__(self, maxim):
        self.maximum = maxim
        self.count = 0
        self.item = 2

    def __iter__(self):
        return self

    def __next__(self):
        c = self.item - 1
        self.count += 1
        if self.count > self.maximum:
            raise StopIteration
        while c > 0:
            if c == 1:
                item = self.item
                self.item += 1
                return item
            elif self.item % c == 0:
                self.item += 1
                c = self.item - 1
            elif self.item % c != 0:
                c -= 1


class PostiveIterator:
    def __init__(self, alist):
        self.count = 0
        self.array = alist

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.array):
            raise StopIteration
        while self.count < len(self.array):
            if self.array[self.count] < 0:
                self.count += 1
            elif self.array[self.count] >= 0:
                self.count += 1
                return self.array[self.count - 1]
        if self.count >= len(self.array):
            raise StopIteration


if __name__ == '__main__':
    t = PostiveIterator([2, -3, 1, 100, -2, 3])
    print(next(t))
    print(next(t))
    print(next(t))
    print(next(t))
