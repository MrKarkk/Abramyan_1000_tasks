a = int(input("A: "))

a3 = a % 10
a2 = (a // 10) % 10
a1 = a // 100

print( str(a3) + str(a1) + str(a2) )