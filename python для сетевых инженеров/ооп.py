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

    def __init__(self,network) -> None:
        self.network = network
        self.allocated = []
        self.hosts = tuple(str(ip) for ip in ipaddress.ip_network(network).hosts())


    def allocate(self,ip):
        if ip in self.hosts:
            if ip not in self.allocated:
                self.allocated.append(ip)
            else:
                raise ValueError(f"IP-adress {ip} уже находится в allocated")
        else:
            raise ValueError(f"IP-adress {ip} alredy isn't in {self.network}")



net1 = Network("10.1.1.0/29")
net1.allocate("10.1.1.1")
net1.allocate("10.1.1.2")

net1.allocated
net1.allocate("10.1.1.100")






#w1 = Switch('sw1','Cisco 3850')

#sw1.generate_interface('Fa',10)
