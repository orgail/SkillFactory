

"""

C:\GitHub\SkillFactory\SkillFactory\Python>cd c:\python38

python.exe -m pip install --upgrade pip




Database Name = home
Pk9O65wTKpc7G7EwYDm3ep8tNgn07OO0
Endpoint
redis-13519.c258.us-east-1-4.ec2.cloud.redislabs.com:13519

Ранее написал бота телеграма:

# бот для задания C5.3
Калькулятор валют # название бота для поиска в телеграмме
t.me/Currency1ToCurrency2_bot
Use this token to access the HTTP API:
1603149288:AAEFlv7bPzTpUTHR9Py76H8zdobeUEy1oM0

# удалил этого бота
t.me/Test_Samara_bot
Use this token to access the HTTP API:
1632604748:AAFNVskmw6NaPWaxNu7ze3tY0G5AfYgpbNE
Keep your token secure and store it safely, it can be used by anyone to control your bot.

# Описание бота
https://core.telegram.org/bots

#----------------------------------------------------------------------------------------
# Особенности работы с интерпритатором -
запустить интерпритатор и оставить включённым -
Вводим в терминале
python -i script.py



#----------------------------------------------------------------------------------------

Создаём виртуальное окружение
# создали проект и папку
mkdir project
cd project
# Ставим окружение
python -m venv venv
# Запускаем окружение
venv\Scripts\activate
env\Scripts\activate

cd project

# Ставим Django
pip3 install Django

# Проверяем установилась ли Django
Python
import django # Ошибок не будет
exit() # выходим

После установки Django создаём пустой проект:
python -m django-admin startproject project

Переходим в папку project в нашем терминале или cmd (если вы на Windows) и прописываем:
python manage.py runserver

Теперь мы можем увидеть сообщение, что наше веб-приложение готово к работе. Открываем любой браузер и переходим по адресу http://127.0.0.1:8000/




#----------------------------------------------------------------------------------------


# print("Hello World")


text=input("Введите какое-то значение: ")
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





def counter(func):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       func(*args, **kwargs)       # Вопрос 1
       count += 1
       print(f"Функция {func} была вызвана {count} раз")
   return wrapper

@counter
def say_word(word):
   print(word)
say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз










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



# Пример рекурсии - число Фибоначи

def fib(n):
    print(n)
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(9))

#---------------------------------------------------------#

# Пример рекурсии - число Фибоначи

def p(n):
    print(n)
    if n == 0:
        return
    else:
        p(n-1)
        print(n)

p(4)


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



class Square:
    def __init__(self, side):
        self.side = side

class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)


sq1 = SquareFactory.create_square(7)
print(sq1.side)




# @property  декоратор
# создадим класс собаки
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age, которое будет переводить возраст животного в человеческий
    @property  # тот самый магический декоратор
    def human_age(self):
        return self.age * 7.3


jane = Dog("jane", 4)
# т.к. метод помечен декоратором property, то нам не надо вызывать этот метод чтобы получить результат
print(jane.human_age)



class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле - шкала счастья
    @property
    def happiness(self):
        return self._happiness

    # с помощью декоратора setter мы можем неявно передать во второй
    # аргумент значение, находящееся справа от равно, а не закидывать это
    # значение в скобки, как мы это делали в модуле C1, когда не знали о
    # декораторах класса
    @happiness.setter
    # допустим, мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
    def happiness(self, value):
        if value <= 100 and value >= 0:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
jane.happiness = 100  # осчастливим нашу собаку < :
print(jane.happiness)




class ParentClass:

    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


# Вызываем методы класса через класс.
ParentClass.method(0)  # ParentClassclassmethod. 0
ParentClass.call_original_method()  # ParentClassclassmethod. 5

ChildClass.method(0)  # ChildClassclassmethod. 0
ChildClass.call_original_method()  # ChildClassclassmethod. 6

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.method(1)  # ParentClassclassmethod. 1
my_obj.call_class_method()  # ParentClassclassmethod. 10



class Square:
    _a = None
    def __init__(self, a):
        self.a = a
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
    @property
    def area(self):
        return self.a**2



try:  # Добавляем конструкцию try-except для отлова нашей ошибки
    print("Перед исключением")
    # теперь пользователь сам вводит числа для деления
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b  # здесь может возникнуть исключение деления на ноль
    print(c)  # печатаем c = a / b если всё хорошо
except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print(e)  # Выводим информацию об ошибке
    print("После исключения")

print("После После исключения")


try:
    *ваш код*
except Ошибка:
    *Код отлова*
else:
    *Код, который выполнится если всё хорошо прошло в блоке try*
finally:
    *Код, который выполнится по любому*


try:
    print("Перед исключением")
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c)  # печатаем c = a / b если всё хорошо
except ZeroDivisionError as e:
    print("После исключения")
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
    print("Всё ништяк")
finally:  # код в блоке finally выполнится в любом случае, при выходе из try-except
    print("Finally на месте")

print("После После исключения")



age = int(input("Сколько тебе лет?"))

if age > 100 or age <= 0:
    raise ValueError("Тебе не может быть столько лет")

print(f"Тебе {age} лет!")  # Возраст выводится только если пользователь ввёл правильный возраст.


try:
    age = int(input("Сколько тебе лет?"))

    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")

    # Возраст выводится только если пользователь ввёл правильный возраст.
    print(f"Тебе {age} лет!")
except ValueError:
    print("Неправильный возраст")


try:
    i = int(input('Введите число:\t'))
except ValueError as e:
    print('Вы ввели неправильное число')
else:
    print(f'Вы ввели {i}')
finally:
    print('Выход из программы')





class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


a = Dot(1, 1)
b = Dot(3, 2)
c = Dot(1, 1)

# print(a.x == c.x and a.y == c.y)
# print(a == c) # Python переписывает на print(a.__eq__(c))
# print(a.__eq__(c))

aa = [Dot(1, 1), Dot(3, 5), Dot(3, 10), Dot(1, 5)]
print(a in aa)

print(aa.count(a))

a = 1
b = 3
print(a.__eq__(b))


# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1


class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        self.y = self.x + 5

# print(B().y)  # ошибка! AttributeError: 'B' object has no attribute 'x'

# правильно:

class B(A):
    def __init__(self):
        super().__init__()  # <- не забудь!
        self.y = self.x + 5

print(B().y)  # 15


try:
    raise ZeroDivisionError  # возбуждаем исключение ZeroDivisionError
except ArithmeticError:  # ловим его родителя
    print("Hello from arithmetic error")


try:
    raise ZeroDivisionError
except ZeroDivisionError:  # сначала пытаемся поймать наследника
    print("Zero division error")
except ArithmeticError:  # потом ловим потомка
    print("Arithmetic error")





class MyException(Exception):  # создаём пустой класс – исключения
    pass

try:
    raise MyException("message")  # поднимаем наше исключение
except MyException as e:  # ловим его за хвост как шкодливого котёнка
    print(e)  # выводим информацию об исключении


# Аббревиатура MRO – method resolution order. А по-русски это переводится как «порядок разрешения методов».
# Но! Тоже самое относится не только к методам, но и к прочим атрибутам класса,
# так как методы – это частный случай более общего понятия «атрибут».

class O: ...
class A(O): ...
class B(O): ...
class C(O): ...
class D(O): ...
class E(O): ...

class K1(A, B, C): ...
class K2(B, D): ...
class K3(C, D, E): ...

class Z(K1, K2, K3): ...

print(Z.mro())
# [<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.A'>, <class '__main__.K2'>, <class '__main__.B'>,
# <class '__main__.K3'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.O'>, <class 'object'>]

# сделаем понагляднее вывод, печатая только имена классов со стрелочками:
def print_mro(T):
    print(*[c.__name__ for c in T.mro()], sep=' -> ')

print_mro(Z)
# Z -> K1 -> A -> K2 -> B -> K3 -> C -> D -> E -> O -> object

class X: ...
class Y: ...
class A(X, Y): ...
class B(Y, X): ...

class MyMRO(type):  # наследование type = это метакласс
    def mro(cls):
        return (cls, A, B, X, Y, object)  # явно задаем порядок!

class G(A, B, metaclass=MyMRO):
    ...

print_mro(G)  # G -> A -> B -> X -> Y -> object
# никаких ошибок!

# Измерение времени @timeit
# Переходим к самописным декораторам.
# Этот декоратор измеряет время выполнения функции, которую декорирует.

import time
from functools import wraps

def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.monotonic()
        result = method(*args, **kw)
        te = time.monotonic()
        ms = (te - ts) * 1000
        all_args = ', '.join(tuple(f'{a!r}' for a in args)
                             + tuple(f'{k}={v!r}' for k, v in kw.items()))
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')
        return result
    return timed


# использование:

@timeit
def slow_func(x, y, sleep):
    time.sleep(sleep)
    return x + y

slow_func(10, 20, sleep=2)
# печатает: slow_func(10, 20, sleep=2): 2004.65 ms




class O:
    def method(self):
        print('I am O')

class A(O):
    def method(self):
        super().method()
        print('I am A')

class B(O):
    def method(self):
        super().method()
        print('I am B')


class C(A, B):
    def method(self):
        super().method()
        print('I am C')

C().method()
print('-------')
A().method()



import os
help(os)


Хорошая структура модуля выглядит следующим образом:

Docstring (описание) модуля.
Область импорта:
импорты системных библиотек;
импорты стандартных пакетов (из PyPI);
импорты ваших модулей (локальных).
Область объявление глобальных констант.
Инициализация модуля.
Область определения функций и классов.
Функции.
if __name__ == '__main__' (метод main) по желанию (это одни из немногих нюансов при работе с собственными модулями).



import math
print(math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3))


import time

i = 10


while i != 0:
    print(i)
    time.sleep(1.0)
    i -= 1
print("Время вышло!")




import unittest

def broken_function():
    raise Exception('Это ошибка')

class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            broken_function()

        self.assertTrue('Это ошибка' in str(context.exception))

if __name__ == '__main__':
    unittest.main()


# список файлов и директорий в папке
import os

print(os.getcwd())
print(os.listdir())  # ['SnapchatLoader', 'FBLoader', 'tmp.py', '.gitignore', 'venv', '.git']

if 'tmp.py' not in os.listdir():
    print("Файл отсутствует в данной директории")

# получить текущий путь
start_path = os.getcwd()
print(start_path)  # /home/nbuser/library
print(os.listdir())

os.chdir("..")  # подняться на один уровень выше
print(os.getcwd())  # '/home/nbuser'
print(os.listdir())

os.chdir(start_path)
print(os.getcwd())  # '/home/nbuser/library'
print(os.listdir())



import os
start_path = os.getcwd()
# соединяет пути с учётом особенностей операционной системы
print(start_path)
print(os.path.join(start_path, 'test'))


f = open('path/to/file', 'filemode', encoding='utf8')



f = open('test.txt', 'w', encoding='utf8')

# Запишем в файл строку
f.write("This is a test string\n")
f.write("This is a new string\n")

f.close()



f = open('test.txt', 'r', encoding='utf8')

print(f.read(10))  # This is a
print(f.read()) # считали остаток файла

f.close()



f = open('test.txt', 'a', encoding='utf8')  # открываем файл на дозапись

sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)  # берет строки из sequence и записывает в файл (без переносов)

f.close()



f = open('test.txt', 'r', encoding='utf8')

print(f.readlines())  # считывает все строки в список и возвращает список

f.close()



f = open('test.txt', 'r', encoding='utf8')

print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline())  # is a new string

f.close()



f = open('test.txt')  # можно перечислять строки в файле
for line in f:
    print(line, end='')

# This is a test string
# This is a new string
# other string
# 123
# test test

f.close()


f = open('test.txt', 'rb')  # можно перечислять строки в файле
print(f.read()) # b'This is a test string\r\nThis is a new string\r\nother string\r\n123\r\ntest test\r\n'
f.seek(0) # смещаемся на 0 позицию
print(f.readlines()) # [b'This is a test string\r\n', b'This is a new string\r\n', b'other string\r\n', b'123\r\n', b'test test\r\n']
f.close()



f = open('input.txt', 'w', encoding='utf8')
sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)  # берет строки из sequence и записывает в файл (без переносов)
f.close()

f = open('input.txt', 'r', encoding='utf8')
s = f.readlines()
print(s)
f.close()

f = open('output.txt', 'w', encoding='utf8')
f.writelines(s)  # берет строки из sequence и записывает в файл (без переносов)
f.close()

f = open('output.txt', 'r', encoding='utf8')
print(f.read())
f.close()

# то же решение
with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in input_file:
           output_file.write(line) # пишет в цикле по одной строке




filename = 'numbers.txt'
output = 'output.txt'

with open(filename) as f:
   min_ = max_ = float(f.readline())  # считали первое число
   for line in f:
       num =  float(line)
       if num > max_:
           max_ = num
       elif num < min_:
           min_ = num

   sum_ = min_ + max_

with open(output, 'w') as f:
   f.write(str(sum_))
   f.write('\n')


# перечитываем файл построчно
# опеределяем оценки как последнй символ строки

count = 0
for line in open("grades.txt", "r", encoding="utf8"):
    points = int(line.split()[-1])
    if points < 3:
        count += 1
        print(line)
print("Количество учащихся с оценками меньше 3: ", count)


with open('grades.txt', 'r', encoding='utf8') as input_file:
   with open('output_grades.txt', 'w') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)

with open('output_grades.txt', 'r', encoding='utf8') as output_file:
    print(output_file.read())


sequence = ["other string\n", "123\n", "test test\n"]
print(list(reversed(sequence)))



from datetime import datetime
import time  # проверять действие измерителя будем с помощью библиотеки time


# вся суть этого измерителя заключается в том, что мы считаем разницу в секундах между открытием и закрытием контекстного менеджера
class Timer:
    def __init__(self):
        pass

    def __enter__(
            self):  # этот метод вызывается при запуске с помощью with. Если вы хотите вернуть какой-то объект, чтобы потом работать с ним в контекстном менеджере, как в примере с файлом, то просто верните этот объект через return
        self.start = datetime.utcnow()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):  # этот метод срабатывает при выходе из контекстного менеджера
        print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")


with Timer():
    time.sleep(2)  # засыпаем на 2 секунды





from datetime import datetime
import time

from contextlib import contextmanager  # импортируем нужный нам декоратор


@contextmanager  # оборачиваем функцию в декоратор contextmanager
def timer():
    start = datetime.utcnow()
    yield  # если вам нужно что-то вернуть через контекстный менеджер, просто вставьте этот объект сюда.
    print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")


with timer():
    time.sleep(2)




class OpenFile:
    def __init__(self, path, type):
        self.file = open(path, type, encoding='utf8')

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('hello.txt', 'wt') as f:
    f.write('Мой контекстный менеджер делает тоже самое!')


import os
print(os.getcwd())




def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)



def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0

print(par_checker('((.)(.))'))
print(par_checker('((.)(.)'))
print(par_checker('((.).))'))




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




a = {}
a = {'(':1}
a['['] = 1

print(a)

a['('] += 1
a['('] += 1
print(a.keys())
print(a.values())


pars = {")": "(", "]": "["}
print(pars[')'])

def par_checker_mod(string):
    stack = []

    for s in string:
        print(stack)
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(par_checker_mod('[]((.)[])'))


print(10%10)








# Создадим класс Queue - нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    # !!! Класс далее нужно дополнить методами !!!

    def is_empty(self):  # очередь пуста?
        # да, если указатели совпадают и в них содержится ноль
        return self.head == self.tail and self.tasks[self.head] == 0

    def size(self):  # получаем размер очереди
        if self.is_empty():  # если она пуста
            return 0  # возвращаем ноль
        elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
            return self.max_size  # значит очередь заполнена
        elif self.head > self.tail:  # если хвост очереди сместился в начало списка
            return self.max_size - self.head + self.tail
        else:  # или если хвост стоит правее начала
            return self.tail - self.head

    def add(self):
        print(self.tasks)
        print(self.head)
        print(self.tail)
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")

        # увеличиваем указатель на 1 по модулю максимального числа элементов
        # для зацикливания очереди в списке
        self.tail = (self.tail + 1) % self.max_size
        print(self.tasks)
        print(self.head)
        print(self.tail)

    def show(self):  # выводим приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} в приоритете")

    def do(self):  # выполняем приоритетную задачу
        print(self.tasks)
        print(self.head)
        print(self.tail)
        print(f"Задача №{self.tasks[self.head]} выполнена")
        # после выполнения зануляем элемент по указателю
        self.tasks[self.head] = 0
        # и циклично перемещаем указатель
        self.head = (self.head + 1) % self.max_size
        print(self.tasks)
        print(self.head)
        print(self.tail)

# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")




# Алгоритм Дейкстры

G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}

print(G.keys())


D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
    print(_) # 1
    print(min_k) # Садовая
    # print(D)
    print(G[min_k]) # {'Сенная площадь': 3, 'Спасская': 3, 'Адмиралтейская': 4, 'Звенигородская': 5}
    print(G[min_k].keys()) # dict_keys(['Сенная площадь', 'Спасская', 'Адмиралтейская', 'Звенигородская'])
    # print(U)

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
        D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
        print(v, D[v], D[min_k], G[min_k][v])
    U[min_k] = True # просмотренную вершину помечаем

print(D)







# задание С4.5.4

# Алгоритм Дейкстры

# здесь эталонное решение без принтов

G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}


D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин
P = {k : None for k in G.keys()} # предки

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
         if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v] # то фиксируем его
            P[v] = min_k # и записываем как предок
    U[min_k] = True # просмотренную вершину помечаем

pointer = 'Владимирская' # куда должны прийти
while pointer is not None: # перемещаемся, пока не придем в стартовую точку
    print(pointer)
    pointer = P[pointer]


# Ответ: Владимирская, Достоевская, Спасская, Садовая, Адмиралтейская




G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}

# print(G.keys())
print(G["Адмиралтейская"].keys())

# к ключам из G приписываем 100 = это будет список D
D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от нее до самой себя равно нулю
# ключам приписываем False, чтобы просмотреть все ключи, это будет список U
U = {k : False for k in G.keys()} # флаги просмотра вершин -

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    # _ - это счётчик от 0 до 7 - все ключи
    print('D', D)
    print('U',U)
    # Перебираем список U со значение False (ещё не просмотренных) и ищём минимум по значениям из списка D
    # D {'Адмиралтейская': 0, 'Садовая': 4, 'Сенная площадь': 100, 'Спасская': 100, 'Звенигородская': 100, 'Пушкинская': 100, 'Владимирская': 100, 'Достоевская': 100}
    # U {'Адмиралтейская': True, 'Садовая': False, 'Сенная площадь': False, 'Спасская': False, 'Звенигородская': False, 'Пушкинская': False, 'Владимирская': False, 'Достоевская': False}
    # Здесь среди False это 'Садовая' = 4
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
    print(_) # 1
    print('min_k', min_k) # Садовая
    # print('k in U.keys()', [k for k in U.keys() if not U[k]])
    # print(D)
    # print(G[min_k]) # {'Сенная площадь': 3, 'Спасская': 3, 'Адмиралтейская': 4, 'Звенигородская': 5}
    # print(G[min_k].keys()) # dict_keys(['Сенная площадь', 'Спасская', 'Адмиралтейская', 'Звенигородская'])
    # print(U)

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
        print('v', v)
        print('D[v]', D[v], '<>', 'D[min_k]', D[min_k], '+', 'G[min_k][v]', G[min_k][v])
        D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
    U[min_k] = True # просмотренную вершину помечаем

print(D)




# Деревья

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    # Смысл в том, что листья - это экземпляры класса, у них есть self.value, но нет потомков
    # листья - это потомки, атрибуты родителя. Чтобы из листа сделать узел, нужно добавить ему потомков
    # пример вызова:
    #
    # создаем корень и его потомки /7|2|5\
    # node_root = BinaryTree(2).insert_left(7).insert_right(5)
    # левое поддерево корня /2|7|6\
    # node_7 = node_root.left_child.insert_left(2).insert_right(6)

    def insert_left(self, next_value):
        # Если у текущего узла нет дочернего слева, то слева делаем подобный нашему класс
        # будет лист, у которого левый и правый потомок is None
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
        # Если слева существует (лист или узел), то создаём новый экземпляр класса,
            new_child = BinaryTree(next_value)
        # в его атрибут - левую ногу кладём имевшееся левое значение
            new_child.left_child = self.left_child
        # теперь полученный новый узел new_child с атрибутом = левым значением кладём в родительскую левую ногу
        # новый узел становится левым потомком текущего узла
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value) # процедура обработки

        if self.left_child is not None: # если левый потомок существует
            self.left_child.pre_order() # рекурсивно вызываем функцию

        if self.right_child is not None: # если правый потомок существует
            self.right_child.pre_order() # рекурсивно вызываем функцию

    def post_order(self):
        if self.left_child is not None: # если левый потомок существует
            self.left_child.post_order() # рекурсивно вызываем функцию

        if self.right_child is not None: # если правый потомок существует
            self.right_child.post_order() # рекурсивно вызываем функцию

        print(self.value) # процедура обработки

    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию


# A_node = BinaryTree('A').insert_left('B').insert_right('C')

# строим дерево

# создаем корень и его потомки /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

# Обход дерева

# префиксный метод обхода
# node_root.pre_order()

# 2, 7, 2, 6, 5, 11, 5, 9, 4

# Постфиксный метод обхода
# node_root.post_order()

# 2, 5, 11, 6, 7, 4, 9, 5, 2

# инфиксный метод обхода
node_root.in_order()

# 2, 7, 5, 6, 11, 2, 5, 4, 9


else:
    new_child = BinaryTree(next_value)
    new_child.left_child = self.left_child
    self.left_child = new_child




# Деревья

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    # Смысл в том, что листья - это экземпляры класса, у них есть self.value, но нет потомков
    # листья - это потомки, атрибуты родителя. Чтобы из листа сделать узел, нужно добавить ему потомков
    # пример вызова:
    #
    # создаем корень и его потомки /7|2|5\
    # node_root = BinaryTree(2).insert_left(7).insert_right(5)
    # левое поддерево корня /2|7|6\
    # node_7 = node_root.left_child.insert_left(2).insert_right(6)

    # def insert_left(self, next_value):
    #     self.left_child = BinaryTree(next_value)
    #     return self

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            # Создаём новый экземпляр с value = 2
            new_child = BinaryTree(next_value)
            # смотрим есть ли потомки у живущей /2|7 слева
            if self.left_child.left_child is not None:
                # если есть, то слева пристраиваем всю цепочку,
                new_child.left_child = self.left_child.left_child
                # то же делаем справа
            if self.left_child.right_child is not None:
                new_child.right_child = self.left_child.right_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        self.right_child = BinaryTree(next_value)
        return self

    def pre_order(self):
        print(self.value) # процедура обработки

        if self.left_child is not None: # если левый потомок существует
            self.left_child.pre_order() # рекурсивно вызываем функцию

        if self.right_child is not None: # если правый потомок существует
            self.right_child.pre_order() # рекурсивно вызываем функцию

    def post_order(self):
        if self.left_child is not None: # если левый потомок существует
            self.left_child.post_order() # рекурсивно вызываем функцию

        if self.right_child is not None: # если правый потомок существует
            self.right_child.post_order() # рекурсивно вызываем функцию

        print(self.value) # процедура обработки

    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию


# A_node = BinaryTree('A').insert_left('B').insert_right('C')

# строим дерево

# создаем корень и его потомки /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

# Обход дерева

# префиксный метод обхода
# node_root.pre_order()

# 2, 7, 2, 6, 5, 11, 5, 9, 4

# Постфиксный метод обхода
# node_root.post_order()

# 2, 5, 11, 6, 7, 4, 9, 5, 2

# инфиксный метод обхода
node_root.in_order()

# 2, 7, 5, 6, 11, 2, 5, 4, 9






array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count=0 ###########
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):  #
        if array[j] < array[idx_min]:
            idx_min = j
        count+=1 ############
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
print(array, count) #####






class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node


    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.first # сохраняем первый элемент
            self.first = self.first.next # меняем указатель на первый элемент
            return node # возвращаем сохраненный

    def popright(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.last # сохраняем последний
            pointer = self.first # создаем указатель
            while pointer.next is not node: # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None # обнуляем указатели, чтобы
            self.last = pointer # предпоследний стал последним
            return node # возвращаем сохраненный

    def __iter__(self): # объявляем класс как итератор
        self.current = self.first # в текущий элемент помещаем первый
        return self # возвращаем итератор

    def __next__(self): # метод перехода
        if self.current is None: # если текущий стал последним
            raise StopIteration # вызываем исключение
        else:
            node = self.current # сохраняем текущий элемент
            self.current = self.current.next # совершаем переход
            return node # и возвращаем сохраненный

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL.__len__())

# -------------------------------------------------------

Линейный алгоритм поиска может применяться для следующих целей:

Нахождение минимального/максимального элемента.
Поиск элемента с определенным значением.
Количество вхождений элемента в массив.
Количество элементов больше заданного.

def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))


# -------------------------------------------------------


# -------------------------------------------------------

# двоичный поиск элемента в отсортированном массиве

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        print('a', middle, array[middle])
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        print('b', middle, array[middle])
        return binary_search(array, element, middle + 1, right)


element = int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 99))

# -------------------------------------------------------



# Наивная сортировка - полный перебор массива наудачу через random, пока не попадётся правильный

import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счетчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count)
# 290698

# -------------------------------------------------------




# Сортировка выбором - ищем меньшее, ставим в начало

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

count = 0

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    print('idx_min', idx_min)
    count +=1
    for j in range(i, len(array)):  #
        if array[j] < array[idx_min]:
            idx_min = j
            print('idx_min от j', idx_min, array[j])
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
        print('i', i, 'array[i]', array[i], 'array[idx_min]', array[idx_min])
print(array)
print(count)

# -------------------------------------------------------


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count=0 ###########
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):  #
        if array[j] < array[idx_min]:
            idx_min = j
        count+=1 ############
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
print(array, count) #####

# -------------------------------------------------------

# Сортировка пузырьком

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        print(j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            print(array)

print(array)


# -------------------------------------------------------
# Сортировка вставками

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count=0

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count += 1
    array[idx] = x

print(array, count)

# -------------------------------------------------------
# алгоритм сортировки слиянием

L = [2, 3, 1, 4, 6, 5, 9, 8, 7]

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(L))


# -------------------------------------------------------

# Быстрая сортировка


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

    return array

print(qsort(array, 7, 2 ))




# -------------------------------------------------------

# Быстрая сортировка

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)






# -------------------------------------------------------

# Сортировка Шелла
# http://aliev.me/runestone/SortSearch/TheShellSort.html

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)





# -------------------------------------------------------

# Пирамидальная сортировка (HeapSort)
# Сортировка кучей.
# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап
        heapify(arr, i, 0)

# Управляющий код для тестирования
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
# Этот код предоставил Mohit Kumra


# -------------------------------------------------------
# Плавная сортировка
# https://habr.com/ru/company/edison/blog/496852/

import random


def smoothsort(lst):
    # Вычислим необходимое количество чисел Леонардо
    leo_nums = leonardo_numbers(len(lst))

    # Куча будет храниться в виде списка деревьев Леонардо
    heap = []

    # Создание первоначальной кучи
    # Очередной элемент или объединяет две предыдущие кучи
    # или добавляет новую кучу из одного узла
    for i in range(len(lst)):
        if len(heap) >= 2 and heap[-2] == heap[-1] + 1:
            heap.pop()
            heap[-1] += 1
        else:
            if len(heap) >= 1 and heap[-1] == 1:
                heap.append(0)
            else:
                heap.append(1)
        restore_heap(lst, i, heap, leo_nums)

    # Разбираем кучу куч
    for i in reversed(range(len(lst))):
        if heap[-1] < 2:
            heap.pop()
        else:
            k = heap.pop()
            t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
            heap.append(k_l)
            restore_heap(lst, t_l, heap, leo_nums)
            heap.append(k_r)
            restore_heap(lst, t_r, heap, leo_nums)


# Генерация чисел Леонардо, не превышающих количество элементов массива
def leonardo_numbers(hi):
    a, b = 1, 1
    numbers = []
    while a <= hi:
        numbers.append(a)
        a, b = b, a + b + 1
    return numbers


# Восстановление кучи после слияния куч или удаления корня
def restore_heap(lst, i, heap, leo_nums):
    # Модифицированная сортировка вставками для корней куч

    current = len(heap) - 1
    k = heap[current]

    while current > 0:
        j = i - leo_nums[k]
        if (lst[j] > lst[i] and
                (k < 2 or lst[j] > lst[i - 1] and lst[j] > lst[i - 2])):
            lst[i], lst[j] = lst[j], lst[i]
            i = j
            current -= 1
            k = heap[current]
        else:
            break

    # Просейка

    while k >= 2:
        t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
        if lst[i] < lst[t_r] or lst[i] < lst[t_l]:
            if lst[t_r] > lst[t_l]:
                lst[i], lst[t_r] = lst[t_r], lst[i]
                i, k = t_r, k_r
            else:
                lst[i], lst[t_l] = lst[t_l], lst[i]
                i, k = t_l, k_l
        else:
            break


# При удалении корня куча делится на две меньшие кучи,
# соответствующие двум предыдущим числами Леонардо
def get_child_trees(i, k, leo_nums):
    t_r, k_r = i - 1, k - 2
    t_l, k_l = t_r - leo_nums[k_r], k - 1
    return t_r, k_r, t_l, k_l


# Основная процедура
def main(n):
    lst = list(range(n))
    random.shuffle(lst)
    print(lst)
    smoothsort(lst)
    print(lst)

# -------------------------------------------------------
Timsort. Обратите на нее особое внимание,
потому что именно эта сортировка используется во встроенных сортировках языка Python.
Она заслуживает рассмотрения, поскольку учитывает еще и эмпирические факты.
https://habr.com/ru/company/infopulse/blog/133303/


# -------------------------------------------------------




import requests

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print(r.content)
print(r.status_code) # узнаем статус полученного ответа



import requests

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler') # попробуем поймать json ответ
print(r.content)
# -------------------------------------------------------


import requests
import json  # импортируем необходимую библиотеку

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50], '\n')




import requests
import json

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

print(d)





import requests

r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
print(r.content)  # содержимое ответа и его обработка происходит также как и с ГЕТ запросами, разницы никакой нету



# -------------------------------------------------------


import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)


# -------------------------------------------------------

import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')

r = json.loads(r.content)

print(r[0])





# -------------------------------------------------------

t.me/Currency1ToCurrency2_bot
Use this token to access the HTTP API:
1603149288:AAEFlv7bPzTpUTHR9Py76H8zdobeUEy1oM0

# -------------------------------------------------------



import telebot

TOKEN = "1603149288:AAEFlv7bPzTpUTHR9Py76H8zdobeUEy1oM0"

# bot.polling(none_stop=True)

# bot.reply_to(message, "This is a message handler")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")

bot = telebot.TeleBot(TOKEN)
# print(bot)

# -------------------------------------------------------


import telebot

TOKEN = '1603149288:AAEFlv7bPzTpUTHR9Py76H8zdobeUEy1oM0'
bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(content_types=['photo', ])
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(content_types=['voice', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'У тебя красивый голос!')
    # bot.reply_to(message.chat.id, 'У тебя красивый голос!')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \n {message.chat.username}")
    print(message.text)


@bot.message_handler()
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, message.text)
    # bot.send_message(message.chat.id, 'hello')


bot.polling(none_stop=True)

# -------------------------------------------------------



import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

tree = lxml.html.document_fromstring(html)
title = tree.xpath(
    '/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

print(title)  # выводим полученный заголовок страницы


# -------------------------------------------------------

import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера.
# Сам html - это то что мы скачали и поместили в папку из браузера.

# print('tree', tree)

ul = tree.findall('body/div[1]/div[3]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# print('ul', ul)

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    print(a.text)  # из этого тега забираем текст - это и будет нашим названием



# -------------------------------------------------------

import lxml.html

html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''

tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')

print(text)





# -------------------------------------------------------

import requests # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

tree = lxml.html.document_fromstring(html)

print('tree', tree)

ul = tree.findall('body/div[1]/div[3]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# print('ul', ul)

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    print(a.text)  # из этого тега забираем текст - это и будет нашим названием




# -------------------------------------------------------


import redis


red = redis.Redis(
    host = 'redis-13519.c258.us-east-1-4.ec2.cloud.redislabs.com',
    port = 13519,
    password = 'Pk9O65wTKpc7G7EwYDm3ep8tNgn07OO0'
)

# запускаем терминал в работу Вводим в терминале
# python -i script.py
# red
# получаем Redis<ConnectionPool<Connection<host=redis-13519.c258.us-east-1-4.ec2.cloud.redislabs.com,port=13519,db=0>>>
# проверяемю, что кэш работает, вводим в терминале:

# red.set('var1', 'value')

# получим значение из кэша:

# red.get('var1')
# выходим - exit()

# затем, после того как вышли снова заходим и снова проверяем наличие данных в кэше red.get('var1') - они должны быть.

print(red.get('var1'))


# -------------------------------------------------------


# пишем в редис словарь

import redis
import json # так так так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?


red = redis.Redis(
    host = 'redis-13519.c258.us-east-1-4.ec2.cloud.redislabs.com',
    port = 13519,
    password = 'Pk9O65wTKpc7G7EwYDm3ep8tNgn07OO0'
)

dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи
red.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1')) # с помощью знакомой нам функции прерващаем данные полученные из кеша обратно в словарь
print(type(converted_dict)) # убеждаемся что мы получили действительно словарь
print(converted_dict) # ну и выводим его содержание


# -------------------------------------------------------

# удаляем из редиса словарь

import redis
import json # так так так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?


red = redis.Redis(
    host = 'redis-13519.c258.us-east-1-4.ec2.cloud.redislabs.com',
    port = 13519,
    password = 'Pk9O65wTKpc7G7EwYDm3ep8tNgn07OO0'
)

red.delete('dict1') # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))



# -------------------------------------------------------

import telebot

TOKEN = '1603149288:AAEFlv7bPzTpUTHR9Py76H8zdobeUEy1oM0'
bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(content_types=['photo', ])
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')

# @bot.message_handler(content_types=['voice', ])
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'У тебя красивый голос!')
#     # bot.reply_to(message.chat.id, 'У тебя красивый голос!')
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Welcome, \n {message.chat.username}")
#     print(message.text)

@bot.message_handler()
def repeat(message: telebot.types.Message):
    # bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'hello')

bot.polling(none_stop=True)



# -------------------------------------------------------


C5.6 примеры решений
https://github.com/depressed-furry/crypto-bot


проблема с библиотекой
https://app.slack.com/client/T016HEPDN72/search/search-1da84d40-b1c4-4091-93a4-e5b07f04e778/thread/C01DLB357TM-1618770952.072300
Попробуйте создать новый проект и добавить в него только pyTelegramBotAPI и запустить в нем этот код:
import telebot
print(telebot.__file__)
print(dir(telebot))


r = requests.get('https://api.exchangeratesapi.io/v1/latest?access_key = 507452a90d133eeff4c02a5be7028ca7&base = USD&symbols=GBP,JPY,EUR')

r = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=507452a90d133eeff4c02a5be7028ca7&base=USD&symbols=GBP')

total_base = json.loads(r.content)[keys[base]]

print(r.content)


(курс из EUR в "B") / (курс из EUR в "A")

print(requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=507452a90d133eeff4c02a5be7028ca7&symbols=JPY,USD').content)

b'{"success":true,"timestamp":1620227644,"base":"EUR","date":"2021-05-05","rates":{"JPY":131.125726,"USD":1.200444}}'

r = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=507452a90d133eeff4c02a5be7028ca7&symbols=JPY,USD')

print(json.loads(r.content)[keys[base]])

print(json.loads(r.content)['base'])

print(json.loads(r.content)['rates'['JPY']])

print(json.loads(r.content)['rates'])

# a = {'success': True, 'timestamp': 1620227644, 'base': 'EUR', 'date': '2021-05-05', 'rates': {'JPY': 131.125726, 'USD': 1.200444}}

# print(a['rates']['JPY'])



# -------------------------------------------------------
b'{"success":true,"timestamp":1620230943,"base":"EUR","date":"2021-05-05","rates":' \
b'{"AED":4.405566,"AFN":93.017537,"ALL":122.883282,"AMD":624.961389,"ANG":2.152951,' \
b'"AOA":784.768971,"ARS":112.458629,"AUD":1.548087,"AWG":2.15961,"AZN":2.036167,' \
b'"BAM":1.95246,"BBD":2.421758,"BDT":101.715007,"BGN":1.95689,"BHD":0.452196,' \
b'"BIF":2352.121317,"BMD":1.19945,"BND":1.601456,"BOB":8.282974,"BRL":6.434684,' \
b'"BSD":1.1994,"BTC":2.0860512e-5,"BTN":88.61068,"BWP":13.045785,"BYN":3.067905,' \
b'"BYR":23509.218672,"BZD":2.417665,"CAD":1.471185,"CDF":2402.498096,"CHF":1.095554,' \
b'"CLF":0.030624,"CLP":845.006147,"CNY":7.764755,"COP":4614.343862,"CRC":737.946436,' \
b'"CUC":1.19945,"CUP":31.785423,"CVE":110.756786,"CZK":25.781877,"DJF":213.551443,' \
b'"DKK":7.43542,"DOP":68.314678,"DZD":160.198392,"EGP":18.797536,"ERN":17.994041,' \
b'"ETB":50.460928,"EUR":1,"FJD":2.446695,"FKP":0.87125,"GBP":0.862417,"GEL":4.1259,' \
b'"GGP":0.87125,"GHS":6.920851,"GIP":0.87125,"GMD":61.435528,"GNF":11898.543135,' \
b'"GTQ":9.256521,"GYD":250.939719,"HKD":9.319468,"HNL":28.936743,"HRK":7.531375,' \
b'"HTG":102.730568,"HUF":358.83706,"IDR":17289.111214,"ILS":3.919227,"IMP":0.87125,' \
b'"INR":88.508968,"IQD":1754.195526,"IRR":50502.839069,"ISK":151.106785,"JEP":0.87125,' \
b'"JMD":182.947432,"JOD":0.850405,"JPY":131.08671,"KES":128.218033,"KGS":101.703042,' \
b'"KHR":4857.772509,"KMF":492.128626,"KPW":1079.50517,"KRW":1350.017092,"KWD":0.36143,' \
b'"KYD":0.999467,"KZT":511.676924,"LAK":11298.818256,"LBP":1832.759371,"LKR":236.314313,' \
b'"LRD":206.395315,"LSL":17.211937,"LTL":3.541664,"LVL":0.725536,"LYD":5.391546,' \
b'"MAD":10.699071,"MDL":21.411946,"MGA":4497.937195,"MKD":61.550221,"MMK":1868.322225,' \
b'"MNT":3419.214809,"MOP":9.599153,"MRO":428.20342,"MUR":48.997795,"MVR":18.411151,' \
b'"MWK":950.566641,"MXN":24.26835,"MYR":4.938734,"MZN":69.280146,"NAD":17.212812,' \
b'"NGN":455.791355,"NIO":42.18446,"NOK":10.030298,"NPR":141.777087,"NZD":1.663571,' \
b'"OMR":0.461781,"PAB":1.1994,"PEN":4.596889,"PGK":4.234651,"PHP":57.597933,' \
b'"PKR":183.575595,"PLN":4.568885,"PYG":8017.030666,"QAR":4.367218,"RON":4.925903,' \
b'"RSD":117.422347,"RUB":89.651326,"RWF":1183.857083,"SAR":4.498509,"SBD":9.545998,' \
b'"SCR":17.955371,"SDG":470.184044,"SEK":10.188038,"SGD":1.602226,"SHP":0.87125,' \
b'"SLL":12276.369689,"SOS":700.479288,"SRD":16.977034,"STD":24863.563207,"SVC":10.49475,' \
b'"SYP":1508.389144,"SZL":17.236435,"THB":37.363063,"TJS":13.680889,"TMT":4.210069,' \
b'"TND":3.297327,"TOP":2.724548,"TRY":9.988061,"TTD":8.142165,"TWD":33.55463,"TZS":2781.524441,' \
b'"UAH":33.248518,"UGX":4272.825754,"USD":1.19945,"UYU":52.642148,"UZS":12612.216426,' \
b'"VEF":256478645698.76993,"VND":27661.114613,"VUV":131.386382,"WST":3.03668,"XAF":654.835044,' \
b'"XAG":0.045344,"XAU":0.000672,"XCD":3.241574,"XDR":0.837765,"XOF":656.098349,"XPF":119.704045,' \
b'"YER":300.271659,"ZAR":17.240701,"ZMK":10796.486936,"ZMW":26.81592,"ZWL":386.223112}}'

# -------------------------------------------------------

"""
# во всей задаче осталось заменить эти 2 строки
# r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
# total_base = json.loads(r.content)[keys[base]] * amount


import requests
import json

quote = 'JPY' # это 1 ещиница валюты, которой определяем стоимость
base = 'USD'



# r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=507452a90d133eeff4c02a5be7028ca7')

# r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
# total_base = json.loads(r.content)[keys[base]] * amount

# print(json.loads(r.content)['rates']['JPY'])

r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=507452a90d133eeff4c02a5be7028ca7&symbols={quote},{base}')
print(r.content)

total_base = json.loads(r.content)['rates'][base] / json.loads(r.content)['rates'][quote] #* amount
print(total_base)

# print(json.loads(r.content)['rates'][quote])
# print(json.loads(r.content)['rates'][base])







# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







# -------------------------------------------------------







# -------------------------------------------------------






# -------------------------------------------------------








# -------------------------------------------------------







































































































































































































































































