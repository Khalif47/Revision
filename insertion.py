def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        k = i - 1
        while k >= 0 and alist[k] > temp:
            alist[k + 1] = alist[k]
            k -= 1

        alist[k + 1] = temp
    return alist


print(insertion_sort([32, 2, 3, 24, 4, 2, 1, 3, 4]))


class NegativeIterators:
    def __init__(self, alist):
        self.list = alist
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.list) <= self.count:
            raise StopIteration
        else:
            while self.list[self.count] < 0 and self.count < len(self.list):
                self.count += 1
        if len(self.list) <= self.count:
            raise StopIteration
        self.count += 1
        return self.list[self.count - 1]


t = NegativeIterators([2, 3, -3, 4, 3,3, 2, 3, ])
for item in t:
    print(item)