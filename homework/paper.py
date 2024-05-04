class Tree():

    _tree_weight = 666

    @staticmethod
    def get_tree_weight():
        return Tree._tree_weight

    def set_tree_weight(weight):
        try:
            Tree._tree_weight = int(weight)
        except:
            print('Не валидное значение')


class Paper():
    _inctance = None
    _paper_weight = 10

    def __new__(cls, *args, **kwargs):
        if Paper._inctance == None:
            if Tree.get_tree_weight() >= cls._paper_weight:
                Tree.set_tree_weight(Tree.get_tree_weight() - Paper._paper_weight)
                Paper._inctance = super().__new__(cls)
            else:
                return None
        else:
            if Paper._paper_weight < BoxPaper._box_paper:
                Paper._inctance = None
                Paper._paper_weight = 10

        return Paper._inctance

    def __init__(self):
        pass

    @staticmethod
    def get_paper_weight():
        return Paper._paper_weight

    def set_paper_weight(weight):
        try:
            Paper._paper_weight = int(weight)
        except:
            print("Не валидное значение")


class BoxPaper(Paper):

    _box_paper = 5.93

    def __new__(cls, *args, **kwargs):
        if Paper.get_paper_weight() >= cls._box_paper:
            Paper.set_paper_weight(Paper.get_paper_weight() - BoxPaper._box_paper)

        return super().__new__(cls)

    @staticmethod
    def get_paper_weight():
        return BoxPaper._box_paper

    def set_paper_weight(weight):
        try:
            BoxPaper._box_paper = int(weight)
        except:
            print("Не валидное значение")


    def __init__(self):
        super().__init__()

for i in range(0,10):
    box = BoxPaper()

    print(f"Tree = {Tree.get_tree_weight()}")
    print(f"Paper = {Paper.get_paper_weight()}")