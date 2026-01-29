a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if abs(a - b) < abs(a - c):
    print(b, abs(a - b))
else:
    print(c, abs(a - c))