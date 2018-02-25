class Sorting:
    def __init__(self, list):
        self.list = list

    def insertion(self):
        n = len(self.list)
        for i in range(1, n):
            temp = self.list[i]
            k = i - 1
            while k >= 0 and self.list[k] > temp:
                self.list[k + 1] = self.list[k]
                k -= 1
            self.list[k + 1] = temp
        return self.list

    def binary_search(self, target):
        start = 0
        end = len(self.list) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.list[mid] == target:
                return mid
            elif self.list[mid] < target:
                start = mid + 1
            elif self.list[mid] > target:
                end = mid - 1
        return None

    def bubble(self):
        n = len(self.list)
        for i in range(n - 1, 0, -1):
            swap = False
            for j in range(i):
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
                    swap = True
            if not swap:
                break
        return self.list

    def selection_sort(self):
        n = len(self.list)
        for k in range(n-1):
            min_pos = self.minimum(k)
            self.list[min_pos], self.list[k] = self.list[k], self.list[min_pos]
        return self.list

    def minimum(self, k):
        n = len(self.list)
        min_element = k
        for i in range(k + 1, n):
            if self.list[min_element] > self.list[i]:
                min_element = i
        return min_element


if __name__ == '__main__':
    t = Sorting([3, 2, 1, 2, 23, 77, -22])
    print(t.selection_sort())
