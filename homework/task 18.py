class Orc:

    def __init__(self,power,intelect,dexterity,health,endurance,level,experience):
    def __init__(self,power,intelect,dexterity):
        self.power = power
        self.intelect = intelect
        self.dexterity = dexterity
        self.health = health
        self.endurance = endurance
        self.level = level
        self.experience = experience
        self.health = 54
        self.endurance = 100
        self.level = 1
        self.experience = 0
        self.use_weapon = "Машет дубинкой"

    def walk(self):
        print("Вперед")

    def right(self):
        print("Прямо")

    def mahat_dubinloi(self):
        if self.endurance > 0:
    def use_weapon(self):
        print("Машет дубинкой")
    def mahat_dubinkoi(self):
        if self.endurance >= 10:
            self.endurance -= 10
            print(f"Махал дубинкой, {self.endurance}")
            print(f"Выносливость = {self.endurance}, Здоровье = {self.health}")
        else:
            self.health -= 10
            print(f"Махал дубинкой, {self.health}")
            tmp = 10 - self.endurance
            self.health -= tmp
            self.endurance = 0
            if self.health <= 0:
                self.die()
            else:
                print(f"Выносливость = {self.endurance}, Здоровье = {self.health}")

    def treated(self):
        if self.treated() < self.health:
            self.treated += 10
            print(f'Лечился {self.treated}')
        max = 100
        if self.health < max:
            self.health += 10
            if self.health >= max:
                self.health = max
            print(f"Лечился, {self.health}")
        else:
            self.health = 100
            print("Вы уже здоровы")

    def upgrade_level(self):
        self.level += 1
        self.experience += 0
        self.experience = 0
        print(f"Апгрейд уровня {self.level}")

    def die(self):
        print("Смерть")

orc = Orc(15,5,5,34,3,0,42)

class Elif(Orc):

    def init(self,power,intelect,dexterity,use_weapon):
        super().__init__(power,intelect,dexterity)
        self.use_weapon() == use_weapon

    def use_weapon(self):
        super().use_weapon()
        print(f"Action = Стреять из лука")

class Person(Orc):

orc.mahat_dubinloi()
    def __init__(self,power,intelect,dexterity):

        super().__init__(power,intelect,dexterity)

