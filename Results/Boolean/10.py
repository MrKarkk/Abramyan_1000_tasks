a = int(input("A: "))
b = int(input("B: "))

res = (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0)

print(res)