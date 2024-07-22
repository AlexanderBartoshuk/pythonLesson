def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key")

def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)
def great(name):
    print(f"hello, {name}!")
    great2(name)
    print(f'getting already to say goodbuy, {name}')
    buy(name)
    
def great2(name):
    print(f"how are you, {name}")
def buy(name):
    print(f"OK, buy, {name}")

print(great("Саша"))
print(great2("alesha"))
print(buy("alex"))


def factorial(x):
    if x== 1:
        return x 
    else:
        return x * factorial(x-1)
    
factorial(5)

