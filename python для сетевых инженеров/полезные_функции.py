# function set 
# Параметр sep контролирует то, какой разделитель будет использоваться между элементами.

print(1,2,3, sep='|')
print(1,2,3, sep='\n')
print(1,2,3, sep=f'\n{'-' * 10}\n')

items = [1,2,3]
print(*items, sep='|')

import time

for num in range(1):
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
