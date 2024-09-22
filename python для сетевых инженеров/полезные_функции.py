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

#                лямда-функция 

def sum_arg(a,b): return a + b
print(sum_arg(5,2)) # - обычная функция 

# лямда фнкция 
sum = lambda a,b: a - b
sum(8,4)

# лямда функция для сортировки 

list_of_tuple = [('IT_VLAN', 320),
                 ('Mngmt_VLAN', 99),
                 ('User_VLAN', 1010),
                 ('DB_VLAN', 11)]
sorted(list_of_tuple,key=lambda x: x[1])


# function map 

# Функция map применяет функцию к каждому элементу
# последовательности и возвращает итератор с результатами.

list_of_numbers = ['one','two','three','four','']
map(str.upper, list_of_numbers)
list(map(str.upper, list_of_numbers))


list_of_str = ["1","2",'3']
list(map(int, list_of_str))

# map + lambda 

vlans = [100,200,300,400,104,507]
list(map(lambda x: "vlans {}".format(x), vlans))

nums = [1, 2, 3, 4, 5]
nums2 = [100, 200, 300, 400, 500]
list(map(lambda x, y: x*y, nums, nums2))

# list comperhention вместо map 

list_of_numbers = ['one','two','three','four','']
[num.upper() for num in list_of_numbers]


list_of_str = [1,2,3,45,43,-1]
[int(x) for x in list_of_str]

# function filter 
# Функция filter применяет функцию ко всем 
# элементам последовательности и возвращает 
# итератор с теми объектами, для которых функция вернула True.

list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
filter(str.isdigit, list_of_strings)

list(filter(str.isdigit, list_of_strings))

list(filter(lambda x: x%2 == 0 , [10, 111, 102, 213, 314, 515,0]))

list_of_word = ['one', 'two', 'list', '', 'dict']
list(filter(lambda x: len(x) > 2, list_of_word))

# list comperhention вместо filter 

list_of_string = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
[w for w in list_of_string if w.isdigit()]

nums = [10, 111, 102, 213, 314, 515]
print([s for s in nums if s % 2 == 1])
print([g for g in nums if g % 2 == 0])

