num = int(input("Number: "))

a1 = num % 10
a2 = (num // 10) % 10
a3 = num // 100

res = ((a1 > a2) and (a2 > a3) or (a3 > a2) and (a2 > a1))

print(res)