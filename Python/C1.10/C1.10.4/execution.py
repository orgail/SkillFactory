# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
# При выводе в консоль вы должны получить:  «Иван Петров, г. Москва, статус "Наставник"»

from Clients import Guests

# Создаём объект для гостей
client_obj = Guests()

# Выводим список гостей
print(client_obj.get_Client())

