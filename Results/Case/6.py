n = int(input("N: "))
a = float(input("A: "))

match n:
    case 1:
        print(a * 0.1)
    case 2:
        print(a * 1000)
    case 3:
        print(a * 1)  
    case 4:
        print(a * 0.001)
    case 5:
        print(a * 0.01) 