class Person():

    def __init__(self,tamina : int, name: str, health: int,treat: int, intellect: int, power: int, dexterity: int, experience: int, level: int, max_health: int ):
        self.name = name
        self.health = health
        self.intellect = intellect
        self.power = power
        self.dexterity = dexterity
        self.tamina = experience
        self.level = level
        self.tamin = tamina
        self.treat = treat
        self.max_health = max_health
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
        if self.treat < self.health:
            self.treat = 10

        if self.health < self.max_health:
            self.health += 10
            print(f"Лечился на {self.treat},текущее здоровье - {self.health}")
            if self.health >= self.max_health:
                self.health = self.max_health
        else:
            self.health = self.max_health
            print("Лечение не требуется, вы уже здоровы")

    def upgrade_level(self):
        self.level += 1
        self.tamina += 0
        self.tamina = 0
        print(f"Апгрейд уровня {self.level}")
    def die(self):
        print("Смерть")




class Orc(Person):

     def __init__(self, name: str):

         super().__init__(100,name,15, 65,20, 0, 1,0,1,132)
     def za_ordu(self):
         print("За Орду!")
         self.die()

     def use_weapon(self): super().use_weapon("Махать дубиной")

class Human(Person):

     def __init__(self, name: str):

         super().__init__(100, name,70, 14,16, 0, 1,0,1,100)

     def za_alians(self):
        print("За Альянс")
        self.die()

     def use_weapon(self):
         super().use_weapon("Махать мечем")

class Elif(Person):

     def __init__(self, name: str):
         super().__init__(90,name,150, 10, 10,30, 90, 100,1,100)


     def za_loreron(self):
         print("За Лордерон")

     def use_weapon(self):
         super().use_weapon("За Лордерон")

orc = Orc("Вася")
human = Human("Петя")
elf = Elif("Нарамакил")
per = Person(90,"Антон",100, 10, 10,30, 90, 100,1,100)
for i in range(0,15):
    elf.use_weapon()

for i in range(0,15):
    elf.treated()
