class Person():

    def __init__(self, name: str, health: int, intellect: int, power: int, dexterity: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.intellect = intellect
        self.power = power
        self.dexterity = dexterity
        self.stamina = 100
        self.level = 1
        self.experience = 0

    def go_direct(self):
        print(self.name, "идет прямо 10 шагов")
    def go_back(self):
        print(self.name, "идет назад 10 шагов")
    def go_right(self):
        print(self.name, "идет вправо 10 шагов")
    def go_left(self):
        print(self.name, "идет влево 10 шагов")
    def use_weapon(self, phrase: str):
        if self.health <= 0:
            self.die()
            return

        if min(self.stamina, 10) == 10:
            self.stamina -= 10
            print(f"{phrase}, {self.stamina}")
        else:
            self.health -= (10 - self.stamina)
            self.stamina = 0

        print(f"{phrase}, stamina = {self.stamina}, health = {self.health}")


    def treated(self):

        if self.health < self.max_health:
            dif = self.max_health - self.health
            hill = min(dif, 10)
            self.health += hill
            print(f"Лечился на {hill},текущее здоровье - {self.health}")
        else:
            print("Лечение не требуется, вы уже здоровы")

    def upgrade_level(self):
        self.level += 1
        self.experience = 0
        print(f"Апгрейд уровня {self.level}")
    def die(self):
        print("Смерть")




class Orc(Person):

     def __init__(self, name: str):

         super().__init__(name, 200,15,65,20 )
     def za_ordu(self):
         print("За Орду!")
         self.die()

     def use_weapon(self): super().use_weapon("Махать дубиной")

class Human(Person):

     def __init__(self, name: str):

         super().__init__(name,150,40, 30,30)

     def za_alians(self):
        print("За Альянс")
        self.die()

     def use_weapon(self):
         super().use_weapon("Махать мечем")

class Elif(Person):

     def __init__(self, name: str):
         super().__init__(name, 100, 60, 15,25)


     def za_loreron(self):
         print("За Лордерон")

     def use_weapon(self):
         super().use_weapon("За Лордерон")

orc = Orc("Вася")
human = Human("Петя")
elf = Elif("Нарамакил")

for i in range(0,15):
    elf.use_weapon()

for i in range(0,15):
    elf.treated()
