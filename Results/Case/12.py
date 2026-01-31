import math

pi = 3.14

num = int(input())
val = float(input())

match num:
    case 1:
        r = val
        d = 2 * r
        l = 2 * pi * r
        s = pi * r * r
        print(f"{d:.2f} {l:.2f} {s:.2f}")
    case 2:
        d = val
        r = d / 2
        l = 2 * pi * r
        s = pi * r * r
        print(f"{r:.2f} {l:.2f} {s:.2f}")
    case 3:
        l = val
        r = l / (2 * pi)
        d = 2 * r
        s = pi * r * r
        print(f"{r:.2f} {d:.2f} {s:.2f}")
    case 4:
        s = val
        r = math.sqrt(s / pi)
        d = 2 * r
        l = 2 * pi * r
        print(f"{r:.2f} {d:.2f} {l:.2f}")
    case _:
        print("Неверный номер")