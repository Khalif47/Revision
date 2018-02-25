
class BinarySearchTreeNode:
    def __init__(self, key, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.result = None

    def collect(self):
        return self

    def _is_empty(self):
        '''
        Checks if the list is empty

        complexity O(N)
        :return:
        '''
        return self.root is None

    def insert(self, key, value):
        '''

        :param key:
        :param value:
        :return:
        :complexity best case O(1) if root item is correct position worst case O(n**2)
        '''
        self.root = self.insert_aux(self.root, key, value)

    def insert_aux(self, current, key, value):
        if current is None:
            current = BinarySearchTreeNode(key)
            current.item = key
            return current
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, value)
            return current
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, value)
            return current
        else:
            current.item = key
            return current

    def search(self, key):
        '''
        searches

        :param key:
        :return:
        :complexity best case O(1) worst case O(N)
        '''
        self.search_aux(self.root, key)
        return self.result

    def search_aux(self, current, key):
        if current is not None:
            if key == current.key:
                self.result = str(current.item)
            elif key < current.key:
                self.search_aux(current.left, key)
            elif key > current.key:
                self.search_aux(current.right, key)

        else:
            raise KeyError('Key not in tree')

    def print_preorder(self):
        '''
        prints everything in the BST including list items

        :return:
        :complexity O(N)
        '''
        self._print_preorder_aux(self.root)

    def _print_preorder_aux(self, current):
        if current is not None:
            print(str(current.key) + ': ' + str(current.item))
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)


    def height(self):
        return self.height_aux(self.root) - 1

    def height_aux(self, current):
        if current is None:
            return 0
        else:
            return 1 + max(self.height_aux(current.left), self.height_aux(current.right))


    def min(self):
        return self.min_aux(self.root)

    def min_aux(self, current):
        if current.left is None:
            return current.item
        else:
            return self.min_aux(current.left)


    def collect_leaves(self):
        alist = []
        return self.collect_leaves_aux(self.root)

    def collect_leaves_aux(self, current):
        if current.left is None and current.right is None:
            return [current.item]
        else:
            if current.left is None:
                return self.collect_leaves_aux(current.right)
            if current.right is None:
                return self.collect_leaves_aux(current.left)
            else:
                return self.collect_leaves_aux(current.left) + self.collect_leaves_aux(current.right)


    def sum_leaves(self):
        return self.sum_leaves_aux(self.root)

    def sum_leaves_aux(self, current):
        if current.left is None and current.right is None:
            return current.item
        else:
            if current.left is None:
                return self.sum_leaves_aux(current.right)
            if current.right is None:
                return self.sum_leaves_aux(current.left)
            else:
                return self.sum_leaves_aux(current.left) + self.sum_leaves_aux(current.right)


    def left(self):
        return self.left_aux(self.root)

    def left_aux(self, current):
        














if __name__ == '__main__':
    t = BinarySearchTree()
    t.insert(14, 'boo')
    t.insert(15, 'res')
    t.insert(13, 'ao')
    t.insert(15, 'me')
    t.insert(15, 'aie')
    t.insert(100, 'no')

    print(t.left())

    t.print_preorder()
