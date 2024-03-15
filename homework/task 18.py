class Orc:

    def __init__(self,power,intelect,dexterity,health,endurance,level,experience):
        self.power = power
        self.intelect = intelect
        self.dexterity = dexterity
        self.health = health
        self.endurance = endurance
        self.level = level
        self.experience = experience

    def walk(self):
        print("Вперед")

    def back(self):
        print("Назад")

    def left(self):
        print("Влево")

    def right(self):
        print("Прямо")

    def mahat_dubinloi(self):
        if self.endurance > 0:
            self.endurance -= 10
            print(f"Махал дубинкой, {self.endurance}")
        else:
            self.health -= 10
            print(f"Махал дубинкой, {self.health}")

    def treated(self):
        if self.treated() < self.health:
            self.treated += 10
            print(f'Лечился {self.treated}')
        else:
            print("Вы уже здоровы")

    def upgrade_level(self):
        self.level += 1
        self.experience += 0
        print(f"Апгрейд уровня {self.level}")

    def die(self):
        print("Смерть")

orc = Orc(15,5,5,34,3,0,42)

orc.mahat_dubinloi()
