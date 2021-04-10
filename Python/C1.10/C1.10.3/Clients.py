# В системе хранится список с данными по клиентам
# для однозначности данных список сейчас будет в одном файле с Классом,
# в дальнейшем импортироваться и сохраняться

clients = [
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


# Класс Clients содержит методы наполнения и получения данных списка клиентов

class Clients:
    def __init__(self, name, balance = 0):
        self.name = str(name)
        self.balance = str(balance)

    def set_clients(self):
        if self.name:
            clients.append({"name": self.name, "balance": int(self.balance)})

    def get_ClientBalance(self):
        for client in clients:
            if client['name'] == self.name:# например 'Иван Петров':
                return (f'Клиент \"{client["name"]}\". Баланс: {client["balance"]} руб.')