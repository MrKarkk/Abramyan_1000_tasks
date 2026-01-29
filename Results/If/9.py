a = int(input("A: "))
b = int(input("B: "))

if a < b:
    print(a, b)
else:
    c = a
    a = b
    b = c
    print(a, b)