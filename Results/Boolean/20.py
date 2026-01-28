num = int(input("N: ")) 

a1 = num % 10
a2 = (num // 10) % 10
a3 = num // 100
res = (a1 != a2) and (a1 != a3) and (a2 != a3)

print(res)