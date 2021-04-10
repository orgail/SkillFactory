# print("Hello World")
"""text=input("Введите какое-то значение: ")
print(text)
print("Ответ на главный вопрос жизни, вселенной и всего такого -", 42)


# Вставьте правильное название функции вместо ???
def which_month():
    month = input("Which month is it now?")
    ???("Current month is", month)


if __name__ == '__main__':
    which_month()
    

first_name = input("Введите ваше имя:")
last_name = input("Введите вашу фамилию:")
age = input("Введите ваш возраст:")
city = input("Введите город проживания:")

# Выводим пустую строку
print("")

# Выводим приветствие, подставляя имя и фамилию пользователя,
# которые он ввел с клавиатуры
print("Привет,", first_name, last_name, "!")

# Выводим пустую строку
print("")

# Выводим фиксированный текст для удобства просмотра
print("Ваш профиль:")

# Выводим возраст и город, которые указал пользователь
print("Возраст:", age, "лет")
print("Город:", city)

colors = 'red green blue'
colors_split = colors.split() # список цветов по-отдельности

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue
colors = 'red green blue'
colors_split = colors.split() # список цветов по-отдельности
print(colors_split)

print('1', colors)
print('2', colors_split)
print(type(colors))
print(type(colors_split))

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
print(type(colors_joined))



s = input("Введите числа через пробел:")
s = s.split()
d = "\n".join(s)
print(d)

age = 25
my_age = "I'm %c years old" % (age) # в шаблоне присутствует специальный символ %d
print(my_age)

day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2

L = ['3.3', '4.4', '5.5', '6.6']

print (list (map (float, L)))

person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
print(person.keys())

print(person.values())
# dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])



d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))


# Напишите программу, которая получает на вход
# название книги, фамилию автора и год выпуска.
# Полученные данные должны быть преобразованы в словарь
# и в таком представлении выведены в консоль.

book = {}
book['BookName'] = input("Название книги")
book['Author'] = input("Фамилия автора")
book['ExtYear'] = input("Год выпуска")
print(book)


abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}


abits = [abit1, abit2, abit3]

  print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True}, {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False}, {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True}]

print(list(str(123456789)))


#----------------------------

# a = 2
# b = 2

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))

#----------------------------
print(bool(0))  # False
print(bool(1))  # True

print(bool("")) # False
print(bool("1"))  # True

print(bool([])) # False
print(bool([1]))  # True

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    if user_database[username] == password:
        return True
    else:
        return False
list_ = [-5, 2, 4, 8, 12, -7, 5, 5]

print(len(list_) == len(set(list_)))

print(len(list_))

print(set(list_))

num = 12345678
print(str(num)[::-1])
print(str(num) == str(num)[::-1])

print(list(range(5)))
# [0, 1, 2, 3, 4]

range(END);
range(START, END);
range(START, END, STEP).

S = 0  # заводим переменную счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

P = 1  # заводим переменную счетчик, в которой мы будем считать сумму
N = 5

for i in range(1, N + 1):
    print("Значение произведение на предыдущем шаге: ", P)
    print("Текущее число: ", i)
    P = P*i
    print("Значение произведения: ", P)
    print("---")
print("Конец цикла")
print("Ответ: произведение равно = ", P)

N = 6

for i in range(1, N + 1):
    print('*'*i)


S = 0  # заводим переменную счетчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число

# заводим цикл while, который будет работать пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную счетчик
    print("Ещё считаю ...")

print("Сумма равна: ", S)
print("Количество чисел: ", n-1)


n = 1
while n**2 < 1000:
    n += 1
print("Искомое число", n - 1)

N = 2
M = 3
# заполнили матрицу последовательными числами
matrix = [
    [0, 1, 2],
    [3, 4, 5],
]


for i in range(N):  # цикл отвечающий за строки
    for j in range(M):  # цикл отвечающий за столбцы
        print(matrix[i][j], end=", ")
# 0 1 2 3 4 5


random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]


min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
        print('index_col = ', index_col)
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Минимальные элементы:", min_value_rows)
print("Их индексы:", min_index_rows)
print("Максимальные элементы:", max_value_rows)
print("Их индексы:", max_index_rows)


list_ = [-5, 2, 4, 8, 12, -7, 5]

for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
    print("Индекс элемента: ", i)
    print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")

list_ = [-5, 2, 4, 8, 12, -7, 5]
# Функция enumerate возвращает данные в виде кортежей,
# где на первом месте стоит индекс, а затем значение
# [(0, -5), (1, 2), (2, 4), ...]
print(list(enumerate(list_)))

for i, value in enumerate(list_):
    print("Индекс элемента: ", i)
    print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")

list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
    if value < 0:
        print("Отрицательное число: ", value)
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", value)
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

text = # здесь добавить тройную кавычку
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.


text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
print(len(text))

count = {}  # для подсчета символов и их количества
for char in text: # мы перебираем переменную text по одному символу присваем этот символ char
   if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
       count[char] += 1
   else:
       count[char] = 1



n = int(input("Введите число\n"))

while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3 + 1) // 2
    print(n)

    if n == 1:
        print("Done")
        break



heads = 35  # количество голов
legs = 94  # количество ног

for r in range(heads + 1):  # количество кроликов
    print('r = ', r)
    for ph in range(heads + 1):  # количество фазанов
        #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
        if (r + ph) > heads or \
            (r * 4 + ph * 2) > legs:
            print('ph = ', ph)
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Количество кроликов", r)
            print("Количество фазанов", ph)
            print("---")

N = 6

for i in range(1, N + 1):
    print('*'*i)

def print_ladder(n):
    for i in range(1, n+1):
        print('*'*i)

n = int(input('Введите число: '))
print_ladder(n)


# здесь добавить тройную кавычку
text = ''' 
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
'''

text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
print(len(text))

count = {}  # для подсчета символов и их количества  - Python понимает, что это  class 'dict' словарь
for char in text: # мы перебираем переменную text по одному символу присваем этот символ char
   if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
       count[char] += 1
   else:
       count[char] = 1

print(count)

for char, cnt in count.items():
   print(f"Символ {char} встречается {cnt} раз")

count = {}  # для подсчета символов и их количества
print(str(type(count)))

def print_2_add_2():
    result = 2+2
    print(result)

print_2_add_2()

def pow_func(base, n=2):
   print(base ** n)

pow_func(3)  # 9
pow_func(5, 3)  # 125

def check_num(a, n):
   if a % n == 0:
       print(f"Число {n} является делителем числа {a}")
   else:
       print(f"Число {n} не является делителем числа {a}")

check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5


def print_ladder(n):
    for i in range(n+1, 1, -1 ):
        print('*'*i)
print_ladder(5)

def pow_func(base, n=2):
   print(base ** n)
print(pow_func(3))
# 9
# None



def check_palindrome(str_):
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       return True
   else:
       return False

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True

def local():
  print(x)  # так как x нет в локальной области видимости, мы берем её из глобальной области

x = 10
local()
print(x)

x = 3
def func():
   print(x)
   x = 5
   x += 5
   return x
print(func())

x = 3
def func():
   global x # объявляем, что переменная является глобальной
   print(x)
   x = 5
   x += 5
   return x
func()
print(x)

a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)
# [[1, 2, 3], 4, 5, 6]

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)
# [1, 2, 3, 4, 5, 6]
print(a) # [1, 2, 3]
print(*a)  # 1 2 3



def my_func(*args, **kwargs):
   print(type(args))
   print(type(kwargs))

my_func()
# <class 'tuple'>
# <class 'dict'>

def adder(*nums):
    sum_ = 0
    for n in nums:
        sum_ += n

    return sum_


print(adder())  # 0
print(adder(1))  # 1
print(adder(1, 2))  # 3
print(adder(1, 2, 3))  # 6

def incorrect_func(name_arg=[]):
   # name_arg является локальной переменной
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
incorrect_func()
print('-----')
incorrect_func()

# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [1]
# Аргумент после изменения [1, 1]



# установим аргумент name_arg пустым а внутри функции будем проверять его
def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[123])

# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]

def get_mul_func(m):
    nonlocal_m = m

    def local_mul(n):
        return n * nonlocal_m

    return local_mul

two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
two_mul(5)  # 5 * 2
print(two_mul(5))

def rec_fibb(n):
   print(n)
   if n == 1:
       return 1
   if n == 2:
      return 1
   return rec_fibb(n - 1) + rec_fibb(n - 2)

print(rec_fibb(5))  # 55

def rec_(n):
   print(n)
   if n == 1:
       return 1
   return n+rec_(n-1)

print(rec_(5))

string = 'convoi'
print(string[:-1])

def reverse_str(string):
   if len(string) == 0:
       return ''
   else:
       print(string[-1])
       return string[-1] + reverse_str(string[:-1])

print(reverse_str('convoi'))


def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

print(sum_digit(11))  # 6

def sum_digit(n):
   if n < 10:
       return n
   else:
       print(n % 10, n // 10)
       return n % 10 + sum_digit(n // 10)

print(sum_digit(235))  # 6




def repeat_list(list_):
   list_values = list_.copy()
   while True:
       value = list_values.pop(0)
       list_values.append(value)
       yield value

for i in repeat_list([1, 2, 3])


str_ = "my tst"
str_iter = iter(str_)

print(type(str_))  # строка
print(type(str_iter))  # итератор строки

# Получим первый элемент строки
print(next(str_iter))  # m

# Получим ещё несколько элементов последовательности
print(next(str_iter))  # y
print(next(str_iter))  #
print(next(str_iter))  # t
print(next(str_iter))  # s
print(next(str_iter))  # t
print(next(str_iter))


age = 25
vug = 17

my_age = "I'm %d years old %d" %(age, vug) # в шаблоне присутствует специальный символ %d

print(my_age)
# I'm 25 years old

a = 0.5
n = 15

s = [a**i for i in range(n+1)]
print(s)

s = sum([a**i for i in range(n+1)])
print(s)


a = [2, 3, 6, 8, 11]

candidate1 = None
candidate2 = None

for elem in a:
    if candidate1 == None or elem > candidate1:
        candidate2 = candidate1
        candidate1 = elem
    elif candidate2 is not None and elem > candidate2:
        candidate2 = elem

print(candidate1,candidate2)


def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, которые будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper


def my_function():
   print("Я - оборачиваемая функция!")
   return 0

print(my_function())
# Я - оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я - оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0



import time


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.15f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458


import time

N = 100


def decorator_time(fn):
   def wrapper():
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       return dt
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
   mean_pow_2 += pow_2()
   mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")



def do_it_twice(func):
    def wrapper():
        func(arg)
        func(arg)
    return wrapper

@do_it_twice
def say_word(word):
    print(word)

say_word("Oo!!!")



# декоратор, в котором встроенная функция умеет принимать аргументы
def do_it_twice(func):
   def wrapper(*args, **kwargs):
       func(*args, **kwargs)
       func(*args, **kwargs)
   return wrapper

@do_it_twice
def say_word(word):
   print(word)

say_word("Oo!!!")
# Oo!!!
# Oo!!!

def make_adder(n):
    def adder(a):
        return a+n
    return adder

adder_10 = make_adder(10)

print(adder_10)

print(adder_10(50))

def make_pow(n):
    def adder(a):
        return a**n
    return adder

adder_3 = make_pow(3)
print(adder_3)
print(adder_3(10))


def rounder(func):
    def wrap(arg1, arg2):
        result = func(arg1, arg2)
        return round(result, 5)

    return wrap


@rounder
def area(height, width):
    return height * width


@rounder
def hypot(a, b):
    return (a ** 2 + b ** 2) ** 0.5


print(area(1.234, 1.72))
print(hypot(10, 3))

def rounder(func):
    def wrap(arg1, arg2, arg3):
        result = func(arg1, arg2, arg3)
        return result
    return wrap

@rounder
def area(height, width, rnd):
    return round((height * width), rnd)

@rounder
def hypot(a, b, rnd):
    return round(((a ** 2 + b ** 2) ** 0.5), rnd)

print(area(1.234, 1.72, 2))
print(hypot(10, 3, 6))

def rounder(func):
    def wrap(arg1):
        result = func(arg1)
        return round(result, 3)
    return wrap

def zero_check(func):
    def wrapper(arg):
        if arg == 0:
            return "На ноль делить нельзя!!!"
        else:
            return func(arg)
    return wrapper

@zero_check
@rounder
def inverse(a):
    return 1 / a


print(inverse(3))
print(inverse(0))

def wrap(*args, **kwargs):
    print(args)
    print(kwargs)

wrap(1, 2, hhh=7)

wrap(a=2, b=7, c=10)

def rounder(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result,3)
    return wrap

@rounder
def inverse(a):
    return 1/a

@rounder
def hypot(a,b):
    return (a**2+b**2)**0.5

print(inverse(0.21))
print(hypot(2,5))

def wrap(n):
    wrap.sum += n
    print(wrap.sum)


wrap.sum = 0
wrap(1)
wrap(1)
wrap(8)
wrap(-2)


a = [1,2,3,10]

iterator = iter(a)

print(next(iterator))
print(next(iterator))
print(next(iterator,"Конец!"))
print(next(iterator,"Конец!"))
print(next(iterator,"Конец!"))


a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1

print(a)





a = 42
b = 42

print(a == b)
# True

print(a is b)
# True

L = ['Hello', 'world']
M = L

print(M is L)
# True



L = ['Hello', 'world']
M = L

print(M is L)
# True

M.append('!')

print(L)
# ['Hello', 'world', '!']

M = L.copy()

print(M is L)
# False

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print( list_id_before == list_id_after )





L = [1,1,2,3,2]
b = list(set(L))
print(b)
# {1,2,3}



text = input("Введите текст:")

unique = set(text)
print(unique)
print("Количество уникальных символов: ", len(unique))

abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов", "Серёгин"}

non_debtors1 = abons.union(debtors)
non_debtors2 = abons.intersection(debtors)
non_debtors3 = abons.difference(debtors)
non_debtors4 = abons.symmetric_difference(debtors)

print(abons)
print(debtors)
print("union")
print(non_debtors1)
print("---")
print("intersection")
print(non_debtors2)
print("---")

print("difference")
print(non_debtors3)
# {'Васильев', 'Иванов'}
print("---")

print("symmetric_difference")
print(non_debtors4)
print("---")



# a = {"Иванов", "Петров", "Васильев", "Антонов"}
#
# b = {"Петров", "Антонов", "Серёгин"}

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

print(type(a))
print(type(b))

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.union(b_set)

print(a_and_b)

some_var = (2,)

if some_var is None:
    print("NoneType")
else:
    print(type(some_var))
print(len(some_var))


a = None # пустая строка
b = a or 1
print(b)




a = "foo"
b = "bar"
print(1 and a or b)

a = ""
b = "bar"
print(1 and a or b)



L = list(map(int, input().split()))

print(all(L))
print (L)


L = [ a for a in some_iter_obj if cond ]


squares = [i**2 for i in range(1,11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (squares)

squares = [i**2 for i in range(1,11) if i % 2 == 1]
# [1, 9, 25, 49, 81]
print (squares)

list_tuples = [(i, i**2) for i in range(1,11)]
#[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
print (list_tuples)



T = [[i*j for j in range(1,11)] for i in range(1,11)]
print(T)

L = [int(input()) for i in range(5)]





M = [[i+j for j in range(5)] for i in range(5)]
#[[0, 1, 2, 3, 4],
# [1, 2, 3, 4, 5],
# [2, 3, 4, 5, 6],
# [3, 4, 5, 6, 7],
# [4, 5, 6, 7, 8]]

print(M)

L = [int(input()) % 2 == 0 for i in range(5)]
print(L)


L = [int(input()) % 2 == 0 for i in range(5)]
print(any(L))

text = 'aaabbccccdaa' #input()  # получаем строку

last = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == last:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += last + str(count)  # иначе - записываем в результат
        last = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += last + str(count)  # и добавляем в результат последний символ
print(result)

L = [i for i in range(10)]
print(L)
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1

G = list(zip(L,M))
print(G)

for a in zip(L,M):
    print(a)
for a, b in zip(L,M):
    print('a =', a, 'b =', b)

N = [a*b for a,b in zip(L,M)]
print(N)



def linear_solve(a, b):
    return b / a
# 2*x = 9
print(linear_solve(0, 1))



# Методом рекурсии находим минимальное значение из списка
L = [12, 2, 5, 1, 8, 11, 10]

def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

print(min_list(L))



# Методом рекурсии зеркалим число

def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

print(mirror(123539))



iter_obj = iter("Hello!")

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))



def fib(n):
    print(n)
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(9))



# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False

result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

def even(x):
    return x % 2 == 0  # функция возвращает только True или False

result = filter(even, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]


# map + filter
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0

print(some_list)
print(list(map(pow2, filter(positive, some_list))))

# list comprehension

print([i**2 for i in some_list if i > 0])


# lambda
print(list(map(lambda x: x ** 2, range(1, 11))))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Сортировка по ключам словаря
d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

# Чтобы отсортировать его по ключам нужно сделать так
print(dict(sorted(d.items())))
# {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

print(dict(sorted(d.items(), key=lambda x: x[1])))



# (вес, рост)
data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

print(list(sorted(data, key=lambda x: x[0]/x[1]**2)))

print(min(data, key=lambda x: x[0]/x[1]**2))


a = ["asd", "bbd", "ddfa", "mcsa"]

# print(list(map(len(a), a)))

print(list(map(len, a)))

print(list(len(a) for a in a)) # это не принято
print(list(map(len, a))) # это принято

print(list(map(lambda i: len(a[i]), range(len(a)))))


a = ["это", "маленький", "текст", "обидно"]

print(list(map(str.upper, a)))

--=======================================

Удалить !!!!

[i+j for j in range(5)] for i in range(5)



random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]


min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
        print('index_col = ', index_col)
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Минимальные элементы:", min_value_rows)
print("Их индексы:", min_index_rows)
print("Максимальные элементы:", max_value_rows)
print("Их индексы:", max_index_rows)

for i in range(N):  # цикл отвечающий за строки
    for j in range(M):  # цикл отвечающий за столбцы
        print(matrix[i][j], end=", ")
# 0 1 2 3 4 5

   [0, 1, 2],

row = [
   ['x', '-', '-'],
   ['x', 'x', 'x'],
   ['o', '-', 'o']
]

for i in range(3):  # цикл отвечающий за строки
    print(i, row[i][0], row[i][1], row[i][2])
    print(i, row[0][i], row[1][i], row[2][i])
print(row[0][0], row[1][1], row[2][2])
print(row[0][2], row[1][1], row[2][0])


def check_win(a):
    if ((row[0][0] == row[1][1] == row[2][2] == a) or (row[0][2] == row[1][1] == row[2][0] == a)):
        print('Победил игрок: ' + a)
        pass
    for i in range(3):  # цикл отвечающий за строки
        if ((row[i][0] == row[i][1] ==  row[i][2] == a) or (row[0][i] == row[1][i] == row[2][i] == a)):
        # if (row[i][0] == row[i][1] == row[i][2]) == 'x') or (row[0][i] == row[1][i] == row[2][i] == 'x'):
        # if True:
            print('Победил игрок: ' + a)
            break


check_win('o')


Замечания по игре:

Функция не возвращает True/False. Возможно, стоит немного попрактиковаться
с возвращаемыми значениями в функциях. Это очень важный блок, который нужен дальше.

Нет обработки выхода за пределы поля:
Игрок O, введите номер строки, куда поставить O: 1
Игрок O, введите номер номер столбца, куда поставить O:4
0 1 2
0 - - -
1 - - x
2 - - -

Есть небольшой совет -не следует использовать глобальные переменные,
это плохая практика. Лучше передавать значения через аргументы функции,
и возвращать результаты функций. Также вместо отдельных функций
для ввода х и о, можно сделать одну с аргументом user, например.



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



class User:
    number_of_fingers = 5
    number_of_eyes = 2

lancelot = User()
print(lancelot.number_of_fingers)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name)
print(julia.email)


x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)



L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))


a = 5
b = 3+2
print(id(a))
print(id(b))

print(id(a) - id(b))



class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False

eggs = Product("eggs", "food", 5)
print(eggs.is_available())



class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id
events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
	              event_type=event.get("type"),
		      session_id=event.get("session_id"))
    print(event_obj.timestamp)





xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(xs)
# sorted(xs.items(), key=lambda x: x[1])
# print(xs)
print(xs.items())
print(list(sorted(xs.items(), key=lambda x: x[1])))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
print(list(sorted(xs.items())))
# print(list(sorted(xs.items(), value=lambda x: x[1])))

>>> x = 1
>>> isinstance(x, int)
# True
>>> x = [1, 2, 3]
>>> isinstance(x, list)
# True
>>> x = (1, 2, 3)
>>> isinstance(x, tuple)
# True

# Проверим, является ли строка 'Hello' одним из типов, описанных в параметре type
>>> isinstance('Hello', (float, int, str, list, dict, tuple))
# True

# Проверка, на принадлежность к экземпляром myObj
class myObj:
  name = "John"

y = myObj()
>>> isinstance(y, myObj)
# True




class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)



class User:
    number_of_fingers = 5
    number_of_eyes = 2

lancelot = User()
print(lancelot.number_of_fingers)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name)
print(julia.email)



class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id
events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
	              event_type=event.get("type"),
		      session_id=event.get("session_id"))
    print(event_obj.timestamp)


class A:
    def some_method(self):
        print('some_method A')

class B(A):
    def some_method(self):
        super().some_method()
        print('some_method B')

x = B()
x.some_method()

"""































































