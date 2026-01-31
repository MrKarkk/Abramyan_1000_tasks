c = input("C: ") 
n = int(input("N: "))


match n:
    case 0:
        print("C")
    case 1:
        match c:
            case 'С':
                print("В")
            case 'В':
                print("Ю")
            case 'Ю':
                print("З")
            case 'З':
                print("С")
    case -1:
        match c:
            case 'С':
                print("З")
            case 'В':
                print("С")
            case 'Ю':
                print("В")
            case 'З':
                print("Ю")