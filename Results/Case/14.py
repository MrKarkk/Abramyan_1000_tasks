import math

num = int(input())
val = float(input())

match num:
    case 1:
        a = val
        r1 = a * math.sqrt(3) / 6
        r2 = 2 * r1
        s = (a * a * math.sqrt(3)) / 4
        print(f"{r1:.2f} {r2:.2f} {s:.2f}")
    case 2:
        r1 = val
        a = (6 * r1) / math.sqrt(3)
        r2 = 2 * r1
        s = (a * a * math.sqrt(3)) / 4
        print(f"{a:.2f} {r2:.2f} {s:.2f}")
    case 3:
        r2 = val
        r1 = r2 / 2
        a = (6 * r1) / math.sqrt(3)
        s = (a * a * math.sqrt(3)) / 4
        print(f"{a:.2f} {r1:.2f} {s:.2f}")
    case 4:
        s = val
        a = math.sqrt(4 * s / math.sqrt(3))
        r1 = a * math.sqrt(3) / 6
        r2 = 2 * r1
        print(f"{a:.2f} {r1:.2f} {r2:.2f}")
    case _:
        print("Неверный номер")