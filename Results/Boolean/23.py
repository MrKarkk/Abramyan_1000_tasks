num = int(input("Number: "))

num4 = num % 10
num3 = (num // 10) % 10
num2 = num // 100 % 10
num1 = (num // 1000) % 10

res = (num1 == num4) and (num2 == num3)

print(res)