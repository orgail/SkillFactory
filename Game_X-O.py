
# Игра "Крестики - Нолики"

# Тестовая матрица
# row = [
#    ['x', '-', 'o'],
#    ['x', '-', 'x'],
#    ['o', '-', '-']
# ]

# ======= Начало игры =======

# Создаём матрицу "Крестики - Нолики"
row = [
   ['-', '-', '-'],
   ['-', '-', '-'],
   ['-', '-', '-']
]

# Функция печати текущей матрицы
def print_matrix():
    print(' ', '0', '1', '2' )
    for i in range(3):
        print(i, row[i][0], row[i][1], row[i][2])

# Переменная контроля окончания игры 0 - продолжаем, 1 - выходим
exit_game = 0

# Функция ввода X
def x_input():
    global x_row, x_col
    x_row = int(input('Игрок Х, введите номер строки, куда поставить Х: ' ))
    x_col = int(input('Игрок Х, введите номер номер столбца, куда поставить Х:' ))

# Функция ввода O
def o_input():
    global o_row, o_col
    o_row = int(input('Игрок O, введите номер строки, куда поставить O: ' ))
    o_col = int(input('Игрок O, введите номер номер столбца, куда поставить O:' ))

# Функция проверки победитея и присвоение 1 переменной окончания игры
def check_win(a):
    global exit_game
    # проверяем диагонали
    if ((row[0][0] == row[1][1] == row[2][2] == a) or (row[0][2] == row[1][1] == row[2][0] == a)):
        exit_game = 1
        print('Победил игрок: ' + a)
        pass
    # проверяем вертикали и горизонтали
    for i in range(3):
        if ((row[i][0] == row[i][1] ==  row[i][2] == a) or (row[0][i] == row[1][i] == row[2][i] == a)):
            exit_game = 1
            print('Победил игрок: ' + a)
            break
# Первичный вывод матрицы
print_matrix()

# Бесконечный цикл игры, пока не будет победителя - exit_game == 1
while True:
# Раздел обработки игры для игрока X
    x_input()
    # Проверка, что ячейка не занята и на неё можно записать значение
    if row[x_row][x_col] == '-':
        row[x_row][x_col] = 'x'
    else:
        print('Ячейка занята, выберите свободную "-" ячейку')
        x_input()

    print_matrix()

    check_win('x')

    if exit_game == 1:
        break

# Раздел обработки игры для игрока O
    o_input()
    # Проверка, что ячейка не занята и на неё можно записать значение
    if row[o_row][o_col] == '-':
        row[o_row][o_col] = 'o'
    else:
        print('Ячейка занята, выберите свободную "-" ячейку')
        o_input()

    print_matrix()

    check_win('o')

    if exit_game == 1:
        break

# ======= Конец игры ========