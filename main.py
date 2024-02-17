def multiply(a,b): return a*b

def print_multiply(a,b,operation):
    result = operation(a,b)
    print(result)

a = 5
b = 4
print_multiply(a,b,multiply)