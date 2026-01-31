y = int(input())

offset = y - 1984

color_index = (offset // 12) % 5

animal_index = offset % 12

match color_index:
    case 0:
        color = 'зеленый'
    case 1:
        color = 'красный'
    case 2:
        color = 'желтый'
    case 3:
        color = 'белый'
    case 4:
        color = 'черный'

match animal_index:
    case 0:
        animal = 'крысы'
    case 1:
        animal = 'коровы'
    case 2:
        animal = 'тигра'
    case 3:
        animal = 'зайца'
    case 4:
        animal = 'дракона'
    case 5:
        animal = 'змеи'
    case 6:
        animal = 'лошади'
    case 7:
        animal = 'овцы'
    case 8:
        animal = 'обезьяны'
    case 9:
        animal = 'курицы'
    case 10:
        animal = 'собаки'
    case 11:
        animal = 'свиньи'

print(f"год {color} {animal}")