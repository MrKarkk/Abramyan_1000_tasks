a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b > c:
    a = a * 2
    b = b * 2
    c = c * 2
    print(a, b, c)
else:
    a = -a
    b = -b
    c = -c
    print(a, b, c)