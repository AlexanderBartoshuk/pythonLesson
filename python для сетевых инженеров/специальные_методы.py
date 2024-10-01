import time
import paramiko
import ipaddress

class CiscoSSH:
    def __init__(self, ip, username, password, enable, disable_paging=True):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=ip,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False)

        self.ssh = self.client.invoke_shell() # если нужно чтобы метод был только внутренний нужно поставить _ перед "ssh"
        self.ssh.send('enable\n')
        self.ssh.send(enable + '\n')
        if disable_paging:
            self.ssh.send('terminal length 0\n')
        time.sleep(1)
        self.ssh.recv(1000)

    def send_show_command(self, command):
        self.ssh.send(command + '\n')
        time.sleep(2)
        result = self.ssh.recv(5000).decode('ascii')
        return result
    

class Switch(object):
    __quantity = 0

    def __configure(self):
        pass 

#dir(Switch)


class A(Switch):
    __quantity =  0

    def __configure(self):
        pass 
    

def modul(a,b):
    return a* b

if __name__ == '__main__':
    print(modul(3,5))

# method __str__ __repr__

class Ipadress:

    def __init__(self,ip) -> None:
        self.ip = ip

    def __str__(self) -> str:

        return f"Ipadress - {self.ip}"
    
    def __repr__(self) -> str:
        return f"Ipadress - {self.ip}"


    def __add__(self,other):

         
        if not isinstance(other, int):
                    raise TypeError(f"unsupported operand type(s) for +:"
                                     f" 'IPAddress' and '{type(other).__name__}'")         
        
        ip_int = int(ipaddress.ip_address(self.ip))
        sum_ip_str = str(ipaddress.ip_address(ip_int + other))
        return Ipadress(sum_ip_str)


ip1 = Ipadress('10.1.1.1')
ip2 = Ipadress('10.2.2.2')

print(ip1 + 5.0)


#ip_adreses = [ip1, ip2]
#print(ip_adreses)
#print
#print(repr(ip2))
#str(ip1)
#
#ipaddress1 = ipaddress.ip_address('10.1.1.1')
#int(ipaddress1)
#
#ipaddress.ip_address(167837953)
