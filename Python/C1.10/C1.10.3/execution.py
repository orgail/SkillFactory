from Clients import ClientsExec

# Имеется два списка клиентов, класс может работать с любым списком

clients_1 = [
    {
     "name": "Иван Петров",
     "balance": 50
    },
    {
     "name": "Сергей Иванов",
     "balance": 30
    },
    {
     "name": "Пётр Сидоров",
     "balance": 40
    }
]

clients_2 = [
    {
     "name": "Иван Сидоров",
     "balance": 10
    },
    {
     "name": "Сергей Петров",
     "balance": 16
    },
    {
     "name": "Пётр Сидоров",
     "balance": 18
    }
]

# Создаём экземпляр класса выбранного списка
client_obj = ClientsExec(clients_1, name = 'Иван Петров')

# Выводим данные по новому клиенту вызовом метода класса
print(client_obj.get_ClientBalance())


# Создадим экземпляр нового клиента с другим списком клиентов
new_client_obj = ClientsExec(clients_2, name = 'Вероника Сидорова', balance = 60)

# Добавляем нового клиента в список клиентов
new_client_obj.set_clients()

# Выводим данные по новому клиенту вызовом метода класса
print(new_client_obj.get_ClientBalance())