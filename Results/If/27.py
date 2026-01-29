x = float(input("X: "))

if x < 0:
    f = 0
elif int(x) % 2 == 0:
    f = 1
else:
    f = -1

print(f)