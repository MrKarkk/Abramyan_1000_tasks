x = int(input("X: "))
y = int(input("Y: "))
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

res = (x1 <= x <= x2) and (y2 <= y <= y1)

print(res)