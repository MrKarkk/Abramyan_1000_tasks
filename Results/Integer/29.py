a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

c_a = int(a / c)
c_b = int(b / c)

s_ab = a * b
s_c = (c_a * c_b) * (c * c)

res = int(s_ab - s_c)

print(res)