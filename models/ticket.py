from .movie import Movie
from .cinema import Cinema

class Ticket:
    def __init__(self, movie: Movie, cinema: Cinema):
        self.movie = movie
        self.cinema = cinema

    def getCinemaName(self)->str:
        return self.cinema.name

    def getRoomCode(self)->str:
        return self.cinema.room.code

    def getSeatNumber(self)->int:
        return self.cinema.room.seat.number

    def getPrice(self)->float:
        return self.movie.price

