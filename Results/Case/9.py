d = int(input("Days number: "))
m = int(input("Month number: "))

d_in_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if d > 1:
    d += 1
else:
    if m < 12:
        m += 1
        d = 1
    else:
        m = 1
        d = 1

print(f"Следующая дата: {d} {m}")

