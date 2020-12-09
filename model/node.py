class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__height = -1
        self.balance = 0

    @property
    def data(self):
        return self.__data

    @property
    def right(self):
        return self.__right

    @property
    def left(self):
        return self.__left

    @data.setter
    def data(self, data):
        self.__data = data

    @right.setter
    def right(self, data):
        self.__right = data

    @left.setter
    def left(self, data):
        self.__left = data
