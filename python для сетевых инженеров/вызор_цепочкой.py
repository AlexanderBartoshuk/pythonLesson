a = "sasha bartoshuk flew to dubai at 10,20,30"
words = a.split()
vlan_str = words[-1]
b = vlan_str.split(',')
print(b)

# или можно в 1 строку 

a = "sasha bartoshuk flew to dubai at 10,20,30"
b = a.split()[-1].split(",")
print(b)

# обязательно должгы быть взаимосвязаны 
