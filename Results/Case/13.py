import math

num = int(input())
val = float(input())

match num:
    case 1:
        a = val
        c = a * math.sqrt(2)
        h = a / math.sqrt(2)
        s = (a * a) / 2
        print(f"{c:.2f} {h:.2f} {s:.2f}")
    case 2:
        c = val
        a = c / math.sqrt(2)
        h = a / math.sqrt(2)
        s = (a * a) / 2
        print(f"{a:.2f} {h:.2f} {s:.2f}")
    case 3:
        h = val
        a = h * math.sqrt(2)
        c = a * math.sqrt(2)
        s = (a * a) / 2
        print(f"{a:.2f} {c:.2f} {s:.2f}")
    case 4:
        s = val
        a = math.sqrt(2 * s)
        c = a * math.sqrt(2)
        h = a / math.sqrt(2)
        print(f"{a:.2f} {c:.2f} {h:.2f}")
    case _:
        print("Неверный номер")