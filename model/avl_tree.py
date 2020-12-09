from model.node import Node


class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    @property
    def height(self):
        if self.node:
            return self.height

    def insert(self, data):
        tree = self.node

        new_node = Node(data)

        if tree == None:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif data.id < tree.data.id:
            self.node.left.insert(data.id)

        elif data.id > tree.data.id:
            self.node.right.insert(data.id)

        else:
            raise("ID [" + str(data.id) + "] already exists in tree.")

        # self.rebalance()

    def rotate_left(self):
       
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T
