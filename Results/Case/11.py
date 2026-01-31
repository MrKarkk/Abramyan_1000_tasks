c = input("C: ") 
n1 = int(input("N1: "))
n2 = int(input("N2: "))

match c:
    case 'С':
        match n1:
            case 1:
                match n2:
                    case 1:
                        print("Ю")
                    case -1:
                        print("С")
                    case 2:
                        print("В")
            case -1:
                match n2:
                    case 1:
                        print("С")
                    case -1:
                        print("Ю")
                    case 2:
                        print("З")
            case 2:
                match n2:
                    case 1:
                        print("В")
                    case -1:
                        print("З")
                    case 2:
                        print("С")
    case 'В':
        match n1:
            case 1:
                match n2:
                    case 1:
                        print("З")
                    case -1:
                        print("В")
                    case 2:
                        print("Ю")
            case -1:
                match n2:
                    case 1:
                        print("В")
                    case -1:
                        print("З")
                    case 2:
                        print("С")
            case 2:
                match n2:
                    case 1:
                        print("Ю")
                    case -1:
                        print("С")
                    case 2:
                        print("В")
    case 'Ю':
        match n1:
            case 1:
                match n2:
                    case 1:
                        print("С")
                    case -1:
                        print("Ю")
                    case 2:
                        print("З")
            case -1:
                match n2:
                    case 1:
                        print("Ю")
                    case -1:
                        print("С")
                    case 2:
                        print("В")
            case 2:
                match n2:
                    case 1:
                        print("З")
                    case -1:
                        print("В")
                    case 2:
                        print("Ю")
    case 'З':
        match n1:
            case 1:
                match n2:
                    case 1:
                        print("В")
                    case -1:
                        print("З")
                    case 2:
                        print("С")
            case -1:
                match n2:
                    case 1:
                        print("З")
                    case -1:
                        print("В")
                    case 2:
                        print("Ю")
            case 2:
                match n2:
                    case 1:
                        print("С")
                    case -1:
                        print("Ю")
                    case 2:
                        print("З")


# Можно было покороче, но так понятнее:

# directions = ['С', 'В', 'Ю', 'З']
# angles = [0, 90, 180, 270]

# c = input("C: ")
# n1 = int(input("N1: "))
# n2 = int(input("N2: "))

# angle = angles[directions.index(c)]

# match n1:
#     case 1:
#         angle = (angle - 90) % 360
#     case -1:
#         angle = (angle + 90) % 360
#     case 2:
#         angle = (angle + 180) % 360
#     case _:
#         print("Неверная команда N1")
#         exit()

# match n2:
#     case 1:
#         angle = (angle - 90) % 360
#     case -1:
#         angle = (angle + 90) % 360
#     case 2:
#         angle = (angle + 180) % 360
#     case _:
#         print("Неверная команда N2")
#         exit()

# final_dir = directions[angles.index(angle)]
# print(final_dir)