class Car():

    def __init__(self, power: int, color: str, weight: int, fuel: str, millage: int, power_reserve: int, mark: str):
        self.power = power
        self.color = color
        self.weight = weight
        self.fuel_type = fuel
        self.millage = millage
        self.power_reserve = power_reserve  # запас хода
        self.km_to_service = millage  # черз сколько обслуживание
        if (power <= 250):
            self.tax = power // 3
        else:
            self.tax = power // 2
        self.mark = mark

    def print_mark(self):
        print(f"Марка авто - {self.mark}")

    def forward(self):
        self.power_reserve -= 10
        if not self.need_fuel_station():
            print("Вперед")

    def back(self):
        print("Задний ход")

    def turn_around(self):
        print("Развернуться")

    def need_fuel_station(self):
        if self.power_reserve >= 30:
            print("Вы можете еще кататься")
            return False
        else:
            if self.power_reserve > 0:
                print(f'Вам следует поехать на заправку и залить {self.fuel_type}')
                return False
            else:
                print("Вы приехали, дальше ехать не можете")
                return True

    def service(self, attention_line: int, red_line: int):
        self.km_to_service -= 100
        if red_line <= self.km_to_service <= attention_line:
            print("Езжай в автосервис, а то я сломаюсь")
        elif self.km_to_service > attention_line:
            print("Вы еще можете кататься и не беспокоиться о своем авто")
        else:
            print("Я сейчас умру, дай мне заехать на обслуживание")

    def tax(self):
        print(f"Твой налог за год составляет {self.tax}")


class SuperCar(Car):

    def __init__(self, power: int, color: str, weight: int, fuel: str, millage: int, power_reserve: int, mark: str):
        super().__init__(power, color, weight, fuel, millage, power_reserve, mark)


class Lamborghini(SuperCar):

    def __init__(self, mark="Lamborghini"):
        super().__init__(500, "Yellow", 2000, "petrol", 463, 43, mark)

    def service(self, attention_line: int, red_line: int): super().service(200, 100)


class Ferrari(SuperCar):

    def __init__(self, color: str):
        super().__init__(612, color, 1233, "petrol", 927, 124, "Ferrari")

    def service(self, attention_line: int, red_line: int): super().service(150, 70)

class Bugatti(SuperCar):

    def __init__(self, mark="Bugatti"):
        super().__init__(1500, "Red", 4895, "petrol", 5683, 823, mark)

    def service(self, attention_line: int, red_line: int): super().service(100, 50)

fera = Ferrari("Black")

for i in range(0, 100):
    fera.forward()
