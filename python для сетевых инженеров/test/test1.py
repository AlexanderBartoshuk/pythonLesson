#config = "switchport trunk allowed vlan 1,3,10,20,30,100"
#con = config.split()
#somn = con[-1]
#c = somn.split(",")
#print(c)


vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
set1 = set(vlans)

sorted(set1)

command1 = {"switchport trunk allowed vlan 1,2,3,5,8"}
command2 = {"switchport trunk allowed vlan 1,3,8,9"}

command1.intersection(command2)


mac = 'AAAA:BBBB:CCCC'
mac_div_str = mac.strip().split(':') 
mac_join_str = "".join(mac_div_str) 
mac_hex = int(mac_join_str, 16)      
mac_bin = bin(mac_hex)      
mac_final = mac_bin.lstrip('0b') 
print(mac_final)                   

