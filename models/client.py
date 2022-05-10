class Client:
    def __init__(self, name: str, cpf: str):
        self.name = name
        self.__cpf = cpf
        self.purchases = []

    def setCpf(self, cpf: str):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf

    def addPurchase(self, purchase):
        self.purchases.append(purchase)