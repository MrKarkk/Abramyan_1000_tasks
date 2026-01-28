x = int(input("X: "))
x1 = int(input("X1: "))
y = int(input("Y: "))
y1 = int(input("Y1: "))

res = (abs(x - x1) == abs(y - y1)) or ((y == y1) or (x == x1))

print(res)