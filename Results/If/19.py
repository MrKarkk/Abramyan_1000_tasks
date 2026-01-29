a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

if a == b == c:
    print(4)
elif a == b == d:
    print(3)
elif a == c == d:
    print(2)
elif b == c == d:
    print(1)