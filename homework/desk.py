class Tree():

    tree_weight = 300

class Board(Tree):

    board_weight = 10

    def __new__(cls, *args, **kwargs):
        if Tree.tree_weight >= cls.board_weight:
            return super().__new__(cls)
        else:
            return None

    def __init__(self):
        Tree.tree_weight -= self.board_weight

class Table(Board):

    table_weight = 5

    def __new__(cls, *args, **kwargs):
        if Board.board_weight >= cls.table_weight:
            return super().__new__(cls)
        else:
            return None

    def __init__(self):
        super().__init__()
        Board.board_weight -= self.table_weight

for i in range(0,10):
    Table()

print(Board.board_weight)
