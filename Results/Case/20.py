d = int(input("Введите день: "))
m = int(input("Введите месяц: "))


match m:
    case 1:
        
        match d:
            case d if d >= 20 and d <= 31:
                print("Водолей")
            case d if d >= 1 and d <= 19:
                print("Козерог")
    case 2:
        match d:
            case d if d >= 19 and d <= 29:
                print("Рыбы")
            case d if d >= 1 and d <= 18:
                print("Водолей")
    case 3:
        match d:
            case d if d >= 21 and d <= 31:
                print("Овен")
            case d if d >= 1 and d <= 20:
                print("Рыбы")
    case 4:
        match d:
            case d if d >= 20 and d <= 30:
                print("Телец")
            case d if d >= 1 and d <= 19:
                print("Овен")
    case 5:
        match d:
            case d if d >= 21 and d <= 31:
                print("Близнецы")
            case d if d >= 1 and d <= 20:
                print("Телец")
    case 6:
        match d:
            case d if d >= 21 and d <= 30:
                print("Рак")
            case d if d >= 1 and d <= 20:
                print("Близнецы")
    case 7:
        match d:
            case d if d >= 23 and d <= 31:
                print("Лев")
            case d if d >= 1 and d <= 22:
                print("Рак")
    case 8:
        match d:
            case d if d >= 23 and d <= 31:
                print("Дева")
            case d if d >= 1 and d <= 22:
                print("Лев")
    case 9:
        match d:
            case d if d >= 23 and d <= 30:
                print("Весы")
            case d if d >= 1 and d <= 22:
                print("Дева")
    case 10:
        match d:
            case d if d >= 23 and d <= 31:
                print("Скорпион")
            case d if d >= 1 and d <= 22:
                print("Весы")
    case 11:
        match d:
            case d if d >= 22 and d <= 30:
                print("Стрелец")
            case d if d >= 1 and d <= 21:
                print("Скорпион")
    case 12:
        match d:
            case d if d >= 22 and d <= 31:
                print("Козерог")
            case d if d >= 1 and d <= 21:
                print("Стрелец")
    case _:
        print("Неверный месяц")