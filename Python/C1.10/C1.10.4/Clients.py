# В системе хранится список с данными по клиентам
# для однозначности данных список сейчас будет в одном файле с Классом,
# в дальнейшем импортироваться и сохраняться

# Класс Clients содержит методы наполнения и получения данных списка клиентов

class Clients:
    def __init__(self, clients, name = "", sity = "", balance = 0, status = ""):
        self.clients = clients
        self.name = str(name)
        self.sity = str(sity)
        self.balance = str(balance)
        self.status = str(status)
        
    def set_clients(self):
        if self.name and self.sity and self.status:
            self.clients.append({"name": self.name, "sity": self.sity, "balance": int(self.balance), "status": self.status})

class ClientsExec(Clients):
    def get_ClientBalance(self):
        for client in self.clients:
            if client['name'] == self.name:# например 'Иван Петров':
                return (f'Клиент \"{client["name"]}\". Баланс: {client["balance"]} руб.')

    def get_Client(self):
        for client in self.clients:
            if client['name'] == self.name:# например 'Иван Петров':
                return (f'Клиент \"{client["name"]}\". Баланс: {client["balance"]} руб.')

# Класс Guests наследует класс Clients,
class Guests(Clients):
# для примера задачи для наследования переопеределим метод get_Client из родительского класса
    def get_Client(self):
        for client in self.clients:
            if client['status'] ==  "Наставник":
                print (f'{client["name"]}, г. {client["sity"]}, статус \"{client["status"]}\"')
        return ""
