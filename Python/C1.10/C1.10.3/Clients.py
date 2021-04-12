# Класс Clients содержит методы наполнения и получения данных списка клиентов

class Clients:
    def __init__(self, clients, name = "", balance = 0):
        self.name = str(name)
        self.balance = str(balance)
        self.clients = clients

    def set_clients(self):
        if self.name:
            self.clients.append({"name": self.name, "balance": int(self.balance)})


class ClientsExec(Clients):
    def get_ClientBalance(self):
        for client in self.clients:
            if client['name'] == self.name:# например 'Иван Петров':
                return (f'Клиент \"{client["name"]}\". Баланс: {client["balance"]} руб.')