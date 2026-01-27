from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)
b = []

i = 0
while i < n:
    b.append(a[i])
    i += 2
print(len(b), b)