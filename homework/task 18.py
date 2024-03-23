class Person():

    def __init__(self,tamina : int, name: str, health: int, intellect: int, power: int, dexterity: int, experience: int, level: int):
        self.name = name
        self.health = health
        self.intellect = intellect
        self.power = power
        self.dexterity = dexterity
        self.tamina = experience
        self.level = level
        self.tamin = tamina
    def go_direct(self):
        print(self.name, "идет прямо 10 шагов")
    def go_back(self):
        print(self.name, "идет назад 10 шагов")
    def go_right(self):
        print(self.name, "идет вправо 10 шагов")
    def go_left(self):
        print(self.name, "идет влево 10 шагов")
    def use_weapon(self, phrase: str):
        if self.tamina >= 10:
            self.tamina -= 10
            print(f"{phrase}, {self.tamina}")
            print(f"Выносливость = {self.tamina}, Здоровье = {self.health}")
        else:
            self.health -= 10
            print(f"{phrase}, {self.health}")
            tmp = 10 - self.tamina
            self.health -= tmp
            self.tamina = 0
            if self.health <= 0:
                self.die()
            else:
                print(f"Выносливость = {self.tamina}, Здоровье = {self.health}")
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
        self.tamina += 0
        self.tamina = 0
        print(f"Апгрейд уровня {self.level}")
    def die(self):
        print("Смерть")

class Orc(Person):

    def __init__(self, name: str):

        super().__init__(100,name,15, 65,20, 0, 1,0)
    def za_ordu(self):
        print("За Орду!")
        self.die()

    def use_weapon(self): super().use_weapon("Махать дубиной")

class Human(Person):

    def __init__(self, name: str):

        super().__init__(100, name,70, 14,16, 0, 1,0)

    def za_alians(self):
       print("За Альянс")
       self.die()

    def use_weapon(self):
        super().use_weapon("Махать мечем")

class Elif(Person):

    def __init__(self, name: str):
        super().__init__(100,name,150, 100, 20,30, 0, 0, )


    def za_loreron(self):
        print("За Лордерон")

    def use_weapon(self):
        super().use_weapon("За Лордерон")

orc = Orc("Вася")
human = Human("Петя")
elf = Elif("Нарамакил")

orc.go_left()
human.go_direct()
elf.za_loreron()
elf.upgrade_level()
elf.use_weapon()