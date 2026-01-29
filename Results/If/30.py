num = int(input("Number: "))

if num % 2 == 0:
    res = "четное "
else:
    res = "нечетное "

if num < 10:
    res += "однозначное "
elif num < 100:
    res += "двузначное "
else:
    res += "трехзначное "

print(res + "число")