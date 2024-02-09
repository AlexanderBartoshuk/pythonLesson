def calculator(num1,num2,action):
    if action == "+":
        return num1 + num2
    elif action == "-":
        return num1-num2
    elif action == "*":
        return num1 * num2
    elif action == "/":
        return num1 / num2

num1 = float(input("The first count is: "))
num2 = float(input("The second count is: "))
action = input("Choose the action: (+ ; - ; * ; / ) ")

result = calculator(num1,num2,action)
print(result)