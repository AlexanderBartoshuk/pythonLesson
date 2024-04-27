class Tree():

    def __init__(self,name,type,locate,year,weight,age):
        self.name = name
        self.location = locate
        self.type = type
        self.year = year
        self.weight = weight
        self.age = age


    def names(self):
        print(f"{self.name} - name of the tree")

    def grow(self):
        print(f'{self.name} is growing')

    def ages(self):
        print(f"Дереву {self.name} {self.age} лет")

    def weights(self, weight: int):
        self.weight += 10
        if self.year >= 20:
            print(f'{self.name} начинает расти')
        elif self.weight >= 300:
            print(f"Дерево-{self.name} уже не может расти")
        else:
            print(f"Дерево еще не выросло")

    def locates(self):
        print(f"{self.name} near with {self.location}")

class Trunk(Tree):
    def __init__(self, name: str):
        super().__init__(name,str,'Rostov-on-Don',23,15)

    def names(self):
        print(f'I am {self.name}')

    def weights(self,weight:int):
        self.weight += 20
        if self.year >= 15:
            print(f'{self.name} начинает расти')
        elif self.weight >= 500:
            print(f"Ствол-{self.name} уже не может расти")
        else:
            print(f"Ствол еще не выросло")




#a = Tree('Тополь','blue','Moscow',1,0,45)
#a.ages()
