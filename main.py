# игра в крестики нолики
def greet():
    print("Приветствуем вас в игре 'Крестики-нолики'")
    print("-----------------------------------------")
    print("Формат ввода: x, y")
    print("x - номер строки")
    print("y - номер столбца")

# вывод поля
def show():
    print(f" 0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")

# запрос у пользователя
def ask():
    while True:
        cords = input("Ваш ход:").split()
        if len(cords) != 2:
            print("Введите 2 координаты")
            continue
        x,y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите число")
            continue
        x,y = int(x),int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапозона")
            continue
        if field[x][y] != "":
            print("Клетка занята")
            continue
        return x,y

# выйгрышная комбинация
def check_win():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cords:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
            if symbols == ["X","X","X"]:
                print("Выйграл крестик")
                return True
            if symbols == ["0","0","0"]:
                print("Выйграл нолик")
                return True
    return False

# игра
greet()
field = [["","",""] for i in range(3)]
lead = 0
while True:
    lead += 1
    show()
    if lead % 2 ==1:
        print("Ход крестика")
    else:
        print("Ход нолика")
    x,y = ask()
    if lead % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():
        break
    if lead == 9:
        print("Ничья")
        break















