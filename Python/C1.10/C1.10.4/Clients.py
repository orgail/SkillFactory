# В системе хранится список с данными по клиентам
# для однозначности данных список сейчас будет в одном файле с Классом,
# в дальнейшем импортироваться и сохраняться

clients = [
    {
     "name": "Иван Петров",
     "sity": "Москва",
     "balance": 50,
     "status": "Наставник"
    },
    {
     "name": "Сергей Иванов",
     "sity": "Челябинск",
     "balance": 30,
     "status": "Покупатель"
    },
    {
     "name": "Пётр Сидоров",
     "sity": "Екатеринбург",
     "balance": 40,
     "status": "Волонтёр"
    }
]

# Класс Clients содержит методы наполнения и получения данных списка клиентов

class Clients:
    def __init__(self, name = "", sity = "", balance = 0, status = ""):
        self.name = str(name)
        self.sity = str(sity)
        self.balance = str(balance)
        self.status = str(status)

    def set_clients(self):
        if self.name and self.sity and self.status:
            clients.append({"name": self.name, "sity": self.sity, "balance": int(self.balance), "status": self.status})

    def get_ClientBalance(self):
        for client in clients:
            if client['name'] == self.name:# например 'Иван Петров':
                return (f'Клиент \"{client["name"]}\". Баланс: {client["balance"]} руб.')

    def get_Client(self):
        for client in clients:
            if client['name'] == self.name:# например 'Иван Петров':
                return (f'Клиент \"{client["name"]}\". Баланс: {client["balance"]} руб.')

# Класс Guests наследует класс Clients,
class Guests(Clients):
# для примера задачи для наследования переопеределим метод get_Client из родительского класса
    def get_Client(self):
        for client in clients:
            if client['status'] ==  "Наставник":
                print (f'{client["name"]}, г. {client["sity"]}, статус \"{client["status"]}\"')
        return ""