def function(name,surname):
    letters = f'письмо для {name} {surname}'
    return letters

    
func= function("alex","bartoshuk")
print(func)

def check_passwd(username, password):
    if len(password) < 8:
        print('Пароль слишком короткий')
        return False
    elif username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
    
# Параметр, который принимает позиционные аргументы
# переменной длины, создается добавлением перед именем 
# параметра звездочки. Имя параметра может быть любым, 
# но по договоренности чаще всего используют имя *args

#Пример функции:


def sum_args(a,*args):
    print(a,args)
    return a + sum(args)
sum_args(1,10,20,30)


#Ключевые аргументы переменной длины
#Параметр, который принимает ключевые аргументы 
#переменной длины, создается добавлением перед именем 
#параметра двух звездочек. Имя параметра может быть любым, 
#но, по договоренности, чаще всего, используют имя **kwargs 
#(от keyword arguments).

def sum_arg(a, **kwargs):
    print(a, kwargs)
    return a + sum(kwargs.values())
sum_arg(a=10, b=20, c=30, d=10)

#                           Распаковка аргументов

items = [1,2,3]
print('One: {}, two: {}, three: {}'.format(*items))

def config_interface(intf_name, ip_address, mask):
    interface = f'interface {intf_name}'
    no_shut = 'no shutdown'
    ip_addr = f'ip address {ip_address} {mask}'
    result = [interface, no_shut, ip_addr]
    return result




interfaces_info = [['Fa0/1', '10.0.1.1', '255.255.255.0'],
                   ['Fa0/2', '10.0.2.1', '255.255.255.0'],
                   ['Fa0/3', '10.0.3.1', '255.255.255.0'],
                   ['Fa0/4', '10.0.4.1', '255.255.255.0'],
                   ['Lo0', '10.0.0.1', '255.255.255.255']]

for info in interfaces_info:
    print(config_interface(*info))
