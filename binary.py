
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
            current.item = value
            current.key = key
            return current
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, value)
            return current
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, value)
            return current
        else:
            current.item = value
            return current



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
        return self.height_aux(self.root)

    def height_aux(self, current):
        if current


if __name__ == '__main__':
    t = BinarySearchTree()
    t.insert(14, 100)
    t.insert(15, 40)
    t.insert(13, 'ao')
    t.insert(15, 'me')
    t.insert(15, 'aie')
    t.insert(100, 'no')

    t.print_preorder()
