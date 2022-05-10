import sys
from models.movie import Movie
from models.purchase import Purchase
from store import Store
sys.path.append("..")
from models.ticket import Ticket
from models.cinema import Cinema
from models.room import Room
from models.seat import Seat

class BuyTicket:
    def __init__(self, data, store: Store):
        seat   = Seat(data['seatNumber'])
        room   = Room(seat, data['roomCode'])
        cinema = Cinema(data['cinemaName'], room)
        movie  = store.findMovie(data['movieId'])

        tickets = []
        tickets.append(Ticket(movie, cinema))
        purchase = Purchase(tickets, store.getAuth())
        store.addPurchase(purchase)
