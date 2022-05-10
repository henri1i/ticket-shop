from store import Store
from models.client import Client
from interface import Displayer
from actions.buyticket import BuyTicket

class Handler:
    SHOW_MOVIES    = 1
    BUY_TICKET     = 2
    LIST_PURCHASES = 3
    EXIT           = 4

    def __init__(self):
        self.store = Store()

    def login(self):
        response = Displayer.renderLoginForm()
        client = Client(response['name'], response['cpf'])
        self.store.setAuth(client)

    def shouldKeepRunning(self, option):
        return True if int(option) != self.EXIT else False

    def handleInput(self, option):
        if (int(option) == self.SHOW_MOVIES):
            self.showMovies()
            return

        if (int(option) == self.BUY_TICKET):
            self.buyTicket()
            return

        if (int(option) == self.LIST_PURCHASES):
            self.listPurchases()
            return
        
    def showMovies(self):
        movies = self.store.getMovies()
    
        Displayer.listMovies(movies)

    def buyTicket(self):
        response = Displayer.renderTicketPurchaseProcess()
        BuyTicket(response, self.store)
        Displayer.renderSuccessfullyPurchased()

    def listPurchases(self):
        purchases = self.store.getPurchases()
        Displayer.renderPurchaseList(purchases)
