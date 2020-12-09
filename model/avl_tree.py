class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    @property
    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0
