from model.node import Node


class AVLTree():
    def __init__(self):
        self.__node = None

    @property
    def node(self):
        return self.__node

    @property
    def height(self):
        if self.__node:
            return self.__node.height
        else:
            return -1

    @node.setter
    def node(self, new_node):
        self.__node = new_node

    def insert(self, key, data=None):
        self.node = self._insert(self.node, key, data)

    def _insert(self, node: Node, key, data=None) -> Node:
        if not node:
            return Node(key, data, balance=0)

        if key < node.key:
            left_sub_root = self._insert(node.left, key, data)
            node.left = left_sub_root
            left_sub_root.parent = node
        elif key > node.key:
            right_sub_root = self._insert(node.right, key, data)
            node.right = right_sub_root
            right_sub_root.parent = node
        else:
            raise Exception("Movie already exists in tree")

        node.balance = self._get_height(
            node.left) - self._get_height(node.right)
        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1

        return self.rebalance(node)

    def rebalance(self, root: Node) -> Node:
        if root.balance == 2:
            if root.left.balance < 0:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            else:
                return self.rotate_right(root)
        elif root.balance == -2:
            if root.right.balance > 0:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:
                return self.rotate_left(root)
        else:
            return root

    def rotate_right(self, node: Node) -> Node:
        pointer = node.left
        tmp = pointer.right

        pointer.right = node
        pointer.parent = node.parent
        node.parent = pointer

        node.left = tmp
        if tmp:
            tmp.parent = node

        if pointer.parent:
            if pointer.parent.left == node:
                pointer.parent.left = pointer
            else:
                pointer.parent.right = pointer

        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1
        node.balance = self._get_height(
            node.left) - self._get_height(node.right)
        pointer.height = max(self._get_height(pointer.left),
                             self._get_height(pointer.right)) + 1
        pointer.balance = self._get_height(
            pointer.left) - self._get_height(pointer.right)

        return pointer

    def rotate_left(self, node: Node) -> Node:
        pointer = node.right
        tmp = pointer.left

        pointer.left = node
        pointer.parent = node.parent
        node.parent = pointer

        node.right = tmp
        if tmp:
            tmp.parent = node

        if pointer.parent:
            if pointer.parent.left == node:
                pointer.parent.left = pointer
            else:
                pointer.parent.right = pointer

        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1
        node.balance = self._get_height(
            node.left) - self._get_height(node.right)

        pointer.height = max(self._get_height(pointer.left),
                             self._get_height(pointer.right)) + 1
        pointer.balance = self._get_height(
            pointer.left) - self._get_height(pointer.right)

        return pointer

    def _get_height(self, node: Node) -> int:
        if not node:
            return 0
        else:
            return node.height

    def _search(self, current, key):
        if not current:
            return

        if current.data.id == key:
            return current.data

        if current.data.id < key:
            return self._search(current.right, key)
        else:
            return self._search(current.left, key)

    def search(self, id):
        movie = self._search(self.node, id)

        if movie:
            return movie
        else:
            raise Exception("Movie not found")

    def _search_by_year(self, current, year, movies):
        if current != None:
            self._search_by_year(current.left, year, movies)
            if current.data.year == year:
                movies.append(current.data)
            self._search_by_year(current.right, year, movies)

    def search_by_year(self, year):
        movies = []

        self._search_by_year(self.node, year, movies)

        return movies

    def _list_by_name(self, current, movies):
        if current != None:
            self.in_order(current.left, movies)
            movies.append(current.data.name)
            self.in_order(current.right, movies)

    def list_by_name(self):
        movies = []
        self.in_order(self.node, movies)
        movies.sort()

        print("Every movie in tree:")
        for movie in movies:
            print(movie)

    def show(self):
        if self.__node:
            self.node.display()
        else:
            raise Exception("Empty tree")
