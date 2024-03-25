class Car():


    def __init__(self, power: int, color: str, weight: int, fuel: str, millage: int, power_reserve: int, mark : str):
        self.power = power
        self.color = color
        self.weight = weight
        self.petrol = fuel
        self.millage = millage
        self.power_reserve = power_reserve
        self.km_to_service = millage
        self.taxi = power // 3
        self.taxis = power // 2
        self.mark = mark


    def name(self):
        print(f"Марка авто - {self.mark}")

    def forward(self):
        print("Вперед")

    def back(self):
        print("Задний ход")

    def turn_around(self):
        print("Развернуться")

    def gas_station(self):
        self.power_reserve -= 10
        if self.power_reserve >= 30:
            print("Вы можете еще кататься")
        else:
            if self.power_reserve > 0:
                print(f'Вам следует поехать на заправку и залить {self.petrol}')
            if self.power_reserve == 0:
                print("Вы приехали, дальше ехать не можете")

    def service(self):

        self.km_to_service -= 100
        if self.km_to_service >= 1000:
            print("Вы еще можете кататься и не беспокоиться о своем авто")
        else:
            if self.km_to_service > 50:
                print("Езжай в автосервис, а то я сломаюсь")
            else:
                print("Я сейчас умру, дай мне заехать на обслуживание")

    def tax(self):
        if self.power <= 250:
            print(f"Твой налог за год составляет {self.taxi}$")
        else:
            if self.power > 250:
                print(f"Твой налог за год составляет {self.taxis}$")


class SuperCar(Car):

    def __init__(self, power: int,color: str, weight: int, fuel: str, millage: int, power_reserve: int, mark : str):
        super().__init__(power,color,weight,fuel,millage,power_reserve,mark)


class Lamborghini(SuperCar):

    def __init__(self,mark="Lamborghini"):
        super().__init__(500,"Yellow",2000,"petrol",463,43,mark)

class Ferrari(SuperCar):

    def __init__(self,mark="Ferrari"):
        super().__init__(612,"Black",1233,"petrol",927,124,mark)

class Bugatti(SuperCar):

    def __init__(self,mark="Bugatti"):
        super().__init__(1500,"Red",4895,"petrol",5683,823,mark)
