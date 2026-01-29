x = float(input("X: "))

if x <= 0:
    f = -x
elif 0 < x < 2:
    f = x**2
else:
    f = 4

print(f)