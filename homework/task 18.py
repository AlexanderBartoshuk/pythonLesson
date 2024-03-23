class Person():

    def __init__(self, name: str, health: int, intellect: int, power: int, dexterity: int, experience: int, lvl: int):
        self.name = name
        self.health = health
        self.intellect = intellect
        self.power = power
        self.dexterity = dexterity
        self.experience = experience
        self.lvl = lvl
    def go_direct(self):
        print(self.name, "идет прямо 10 шагов")
    def go_back(self):
        print(self.name, "идет назад 10 шагов")
    def go_right(self):
        print(self.name, "идет вправо 10 шагов")
    def go_left(self):
        print(self.name, "идет влево 10 шагов")
    def use_weapon(self, phrase: str):
        if self.experience >= 10:
            self.experience -= 10
            print(f"{phrase}, {self.experience}")
            print(f"Выносливость = {self.experience}, Здоровье = {self.health}")
        else:
            self.health -= 10
            print(f"{phrase}, {self.health}")
            tmp = 10 - self.experience
            self.health -= tmp
            self.experience = 0
            if self.health <= 0:
                self.die()
            else:
                print(f"Выносливость = {self.experience}, Здоровье = {self.health}")
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

class Orc(Person):

    def __init__(self, name: str):
        super().__init__(name,100, 15, 65,20, 0, 1)
    def za_ordu(self):
        print("За Орду!")
        self.die()

    def use_weapon(self): super().use_weapon("Махать дубиной")




