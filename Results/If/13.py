a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if (a > b and b > c) or ((a > c and c > b)):
    print(a)
elif (b > a and a > c) or (b > c and c > a):
    print(b)
elif (c > a and a > b) or (c > b and b > a):
    print(c)

# Можно было проще: (a + b + c) - min(a, b, c) - max(a, b, c)