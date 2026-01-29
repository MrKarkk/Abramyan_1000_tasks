num = int(input("Number: "))

if num == 0:
    print("нулевое число")
else:
    if num > 0:
        res = "положительное "
    else:
        res = "отрицательное "

    if num % 2 == 0:
        res += "четное число"
    else:
        res += "нечетное число"
    print(res)