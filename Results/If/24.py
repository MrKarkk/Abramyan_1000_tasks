import math

x = float(input("X: "))

if x > 0:
    f = 2 * math.sin(x)
else:
    f = 6 - x

print(f) 