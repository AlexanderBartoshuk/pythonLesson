def task3():
    count=0
    def count_digit(num):
        global count
        if (num >0):
            if(num%10==0):
                count +=1
            count_digit(num // 10)
        return count
    n=int(input("Введите число:"))

    print("количество нулей в числе:",count_digit(n))

