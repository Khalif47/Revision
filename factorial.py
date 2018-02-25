def contains(self, item):
    return contains_aux(item, self.head)


def contains_aux(self, item, current):
    if current is None:
        return False
    elif current.item == item:
        return True
    else:
        return self.contains_aux(item, current.next)


def append_rear(self, item):
    if self.is_full():
        return False
    else:
        self.array[self.rear] = item
        self.rear = selr.rear + 1) % self.tablesize
        self.count += 1


