a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if (a < b and a < c) or (a == b and a < c) or (a == c and a < b) or (a < b and a == c):
    print(a)
elif (b < a and b < c) or (b == a and b < c) or (b < a and b == c):
    print(b)
elif (c < a and c < b) or (c == a and c < b) or (c == b and c < a):
    print(c)

# Можно было проще: res = min(a, b, c)