num = int(input("Number: "))

a1 = num % 10
a2 = (num // 10) % 10
a3 = num // 100

res = a3 < a2 < a1

print(res)