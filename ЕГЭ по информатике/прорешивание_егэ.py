#
#
#for n in range(256):
#    s = bin(n)[2:]  # перевод в двоичную систему
#    s = str(s)
#    if len(s) < 8: 
#        s = '0' * (8 - len(s))+s
#    s = s.replace('1', '*')
#    s = s.replace('0', '1')
#    s = s.replace('*', '0')
#    r = int(s,2)
#    if n-r == 133:
#        print(r)
#
        
for n in range(0, 256):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = 11111111 - int(s)
    s = int(str(s),2)
    s = s-n
    if s == 133:
        print(n)


