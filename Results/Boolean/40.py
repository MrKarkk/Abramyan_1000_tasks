x = int(input("X: "))
x1 = int(input("X1: "))
y = int(input("Y: "))
y1 = int(input("Y1: "))

res_x = abs(x - x1)
res_y = abs(y - y1)

res = (res_x == 1 and res_y == 2) or (res_x == 2 and res_y == 1)

print(res)