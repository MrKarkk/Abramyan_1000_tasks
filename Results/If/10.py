a = int(input("A: "))
b = int(input("B: "))

if a != b:
    c = a + b
    a = c
    b = c
    print(a, b)
elif a == b:
    a = 0
    b = 0
    print(a, b)