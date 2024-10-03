#s = "string"
#print(s.upper())
#
#print(s.center(20,'"'))
import ipaddress


class Switch:

    def __init__(self,hostname,model) -> None:
        self.model = model
        self.hostname = hostname


    def info(self):
        print('Hostname: {}\nModel: {}'.format(self.hostname,self.model))


    def generate_interface(self,intf_type,number_of_intf):
        interfaces = [f"{intf_type}{number}" for number in range(1, number_of_intf + 1)]
        self.interfaces = interfaces


class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]

    def __iter__(self):
        return iter(self.addresses)

    

# Протоколы
# Протокол - это набор методов, которые должны быть реализованы в объекте,
# чтобы он поддерживал определенное поведение.

class Items:

    def __init__(self,items) -> None:
        self.items = items

    def __getitem__(self,index):
        print('Вызываю __getitem__')
        return self.items[index]
    

    
iterable = Items([1,3,4,2,6,5])
iterable[2]

for i in iterable:
    print(">>>", i )

list(map(str, iterable))

def my_for(iterable):
    if getattr(iterable, "__iter__", None):
        print('Есть __iter__')
        iterator = iter(iterable)
        while True:
            try:
                print(next(iterator))
            except StopIteration:
                break
    elif getattr(iterable, "__getitem__", None):
        print('Нет __iter__, но есть __getitem__')
        index = 0
        while True:
            try:
                print(iterable[index])
                index += 1
            except IndexError:
                break
iterable = Items([1,3,4,2,6,5])
my_for([1,2,3,4])



net1 = Network('10.1.1.192/30')
for ip in net1:
    print(ip)
