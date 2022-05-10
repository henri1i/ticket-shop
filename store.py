from models.purchase import Purchase
from seeders.cinemaseeder import CinemaSeeder
from seeders.movieseeder import MovieSeeder
from models.client import Client
from models.movie import Movie

class Store:
    def __init__(self, movieCount = 5):
        self.__movies = MovieSeeder.getMovies(movieCount)
        self.__purchases = []
    
    def findMovie(self, movieId: int)->Movie:
        for movie in self.__movies:
            if (movie.id == int(movieId)):
                return movie

    def getMovies(self)->list:
        return self.__movies


    def setAuth(self, client: Client):
        self.__auth = client

    def getAuth(self)->Client:
        return self.__auth


    def addPurchase(self, purchase: Purchase):
        self.__purchases.append(purchase)

    def getPurchases(self)->list:
        return self.__purchases