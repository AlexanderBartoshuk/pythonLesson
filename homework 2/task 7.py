def task7():
    def userInput():
        try:
            num1 = float(input("The first count is: "))
            num2 = float(input("The second count is: "))
            action = input("Choose the action: (+ ; - ; * ; / ) ")
            print("result:", calculator(num1, num2, action))
        except:
            print("Incorrect number format, please try again")
            userInput()

    def calculator(num1, num2, action):
        if action == "+":
            return num1 + num2
        elif action == "-":
            return num1 - num2
        elif action == "*":
            return num1 * num2
        elif action == "/":
            return num1 / num2
        else:
            print("incorrect input!!, please try again:")
            userInput()