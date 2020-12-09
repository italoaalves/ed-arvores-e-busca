from model.node import Node


class AVLTree():
    def __init__(self):
        self.node = None
        self.__height = -1
        self.balance = 0

    @property
    def height(self):
        if self.node:
            return self.__height
        else:
            return - 1

    def insert(self, data):
        tree = self.node

        new_node = Node(data)

        if tree == None:
            self.node = new_node
            self.node.left = Node()
            self.node.right = Node()

        elif data.id < tree.data.id:
            self.node.left.insert(data)

        elif data.id > tree.data.id:
            self.node.right.insert(data)

        else:
            raise("ID [" + str(data.id) + "] already exists in tree.")

        self.rebalance()

    def rotate_left(self):
        A = self.node
        B = self.node.right.node
        T = B.left.node
        self.node = B
        B.left.node = A
        A.right.node = T

    def rotate_right(self):
        A = self.node
        B = self.node.left.node
        T = B.right.node
        self.node = B
        B.right.node = A
        A.left.node = T

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.__height = max(self.node.left.height,
                                self.node.right.height) + 1
        else:
            self.__height = -1

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def is_leaf(self):
        return (self.height == 0)

    def show(self, level=0, pref=''):
        self.update_heights()
        self.update_balances()

        if(self.node != None):
            print('-' * level * 2, pref, self.node.data.id, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.show(level + 1, '<')
            if self.node.left != None:
                self.node.right.show(level + 1, '>')

    def _search_in_order(self, current, year, movies):
        if current != None:
            self._search_in_order(current.node.left, year, movies)
            if current.node.data.year == year:
                movies.append(current.node.data)
            self._search_in_order(current.node.right, year, movies)

    def search_by_year(self, year):
        movies = []

        self._search_in_order(self.node, year, movies)

        return movies
