from .ticket import Ticket
from .client import Client

class Purchase:
    def __init__(self, items: list, client: Client):
        self.__items = items
        self.client = client

    def getItems(self):
        return self.__items

    def getTotalPrice(self):
        totalPrice = 0
    
        for item in self.__items:
            totalPrice += item.price

    def insertItem(self, item: Ticket):
        self.__items.append(item)

    def removeItem(self, item_id: int):
        self.__items = filter(lambda item: id(item) == item_id, self.__items)