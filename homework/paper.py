class Tree():

    tree_weight = 663.34

class Paper(Tree):

    paper_weight = 40

    def __new__(cls, *args, **kwargs):
        if Tree.tree_weight >= cls.paper_weight:
            return super().__new__(cls)
        else:
            return None

    def __init__(self):
        Tree.tree_weight -= self.paper_weight

class BoxPaper(Paper):

    box_paper = 5.93

    def __new__(cls, *args, **kwargs):
        if Paper.paper_weight >= cls.box_paper:
            return super().__new__(cls)
        else:
            return None

    def __init__(self):
        super().__init__()
        Paper.paper_weight -= self.box_paper

