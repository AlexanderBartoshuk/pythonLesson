# function set 
# Параметр sep контролирует то, какой разделитель будет использоваться между элементами.

print(1,2,3, sep='|')
print(1,2,3, sep='\n')
print(1,2,3, sep=f'\n{'-' * 10}\n')

items = [1,2,3]
print(*items, sep='|')

import time

for num in range(0):
    print(num + 1, end=' ')
    time.sleep(1)

# Функция sorted
list_of_words = ['one', 'two', 'list', '', 'dict', '2',"3"]
sorted(list_of_words)

# reverse
# Флаг reverse позволяет управлять порядком сортировки.
# По умолчанию сортировка будет по возрастанию элементов.

sorted(list_of_words, reverse=True)

#key
#С помощью параметра key можно указывать, как именно выполнять сортировку.
#Параметр key ожидает функцию, с помощью которой должно быть выполнено сравнение.

sorted(list_of_words, key=len)


# enumerate 

list1 = ['str1', 'str2', 'str3']

#for position, string in enumerate(list1, 100):
#    print(position, string)

list(enumerate(list1,100))


#                       zip 

a = [1,2,3,4]
b = [100,200,300,400]
c = [2,4,6,8]
list(zip(a,b,c))



d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']

list(zip(d_keys,d_values))


#               function all


ip = '10.0.1.1'

all(i.isdigit for i in ip.split('.'))

#               function any 

def ignore_command(command):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    * command - строка. Команда, которую надо проверить
    * Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    ignore = ['duplex', 'alias', 'Current configuration']

    for word in ignore:
        if word in command:
            return True
    return False

ignore_command("alias")