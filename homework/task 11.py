
def homework(n):
    if n == 0:
        return ""
    else:
        return homework(n // 2) + str(n % 2)

print(homework(100))
