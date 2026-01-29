a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and a > c and b > c and b < a:
    print(a + b)
elif b > c and c > a and a < b and a < c:
    print(b + c)
elif c > a and a > b and b < c and b < a:
    print(c + a)

# Можно было проще: (a + b + c) - min(a, b, c)