x = int(input("X: "))
x1 = int(input("X1: "))
y = int(input("Y: "))
y1 = int(input("Y1: "))

res = ((x + y) % 2 == 0) and ((x1 + y1) % 2 == 0)

print(res)