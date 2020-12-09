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

    def _insert(self, node, key, data=None):
        if not node:
            return Node(key, data, balance=0)

        if key < node.key:
            left_node = self._insert(node.left, key, data)
            node.left = left_node
            left_node.parent = node
        elif key > node.key:
            right_node = self._insert(node.right, key, data)
            node.right = right_node
            right_node.parent = node
        else:
            raise Exception("Movie already exists in tree")

        node.balance = self._get_height(
            node.left) - self._get_height(node.right)
        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1

        return self.rebalance(node)

    def rebalance(self, node):
        if node.balance == 2:
            if node.left.balance < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            else:
                return self.rotate_right(node)
        elif node.balance == -2:
            if node.right.balance > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
            else:
                return self.rotate_left(node)
        else:
            return node

    def rotate_right(self, node):
        pointer = node.left
        aux = pointer.right

        pointer.right = node
        pointer.parent = node.parent
        node.parent = pointer

        node.left = aux
        if aux:
            aux.parent = node

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

    def rotate_left(self, node):
        pointer = node.right
        aux = pointer.left

        pointer.left = node
        pointer.parent = node.parent
        node.parent = pointer

        node.right = aux
        if aux:
            aux.parent = node

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
            self._list_by_name(current.left, movies)
            movies.append(current.data.name)
            self._list_by_name(current.right, movies)

    def list_by_name(self):
        movies = []
        self._list_by_name(self.node, movies)
        movies.sort()

        return movies

    def show(self):
        if self.__node:
            self.node.display()
        else:
            raise Exception("Empty tree")
