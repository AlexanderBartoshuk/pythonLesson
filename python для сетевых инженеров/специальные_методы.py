import time
import paramiko


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

