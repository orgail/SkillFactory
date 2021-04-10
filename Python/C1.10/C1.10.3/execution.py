from Clients import Clients

# Создаём объект по необходимому клиенту
client_obj = Clients(name = 'Иван Петров')

# Выводим данные по нужному клиенту вызовом метода класса
print(client_obj.get_ClientBalance())

# Добавляем создадим экземпляр нового клиента
new_client_obj = Clients(name = 'Вероника Сидорова', balance = 60)

# Добавляем нового клиента в список клиентов
new_client_obj.set_clients()

# Выводим данные по новому клиенту вызовом метода класса
print(new_client_obj.get_ClientBalance())