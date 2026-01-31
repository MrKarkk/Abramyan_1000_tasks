n = int(input("N: "))
a = int(input("A: "))
b = int(input("B: "))

match n:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
        print(a / b)