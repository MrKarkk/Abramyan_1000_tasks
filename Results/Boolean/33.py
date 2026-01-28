a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

res = a + b > c and a + c > b and b + c > a

print(res)