from .faker import Faker
import sys
sys.path.append("..")
from models.movie import Movie
from models.threedimensionalmovie import ThreeDimensionalMovie

class MovieSeeder:
    @staticmethod
    def getMovies(count: int):
        fakeMovies = Faker.getRandomData(count, 'data/movies.json')

        movies = []
        for i in range(count):
            data = fakeMovies[i]
            if (data['type'] == 1):
                movies.append(Movie(data['id'], data['name'], data['generes'], data['rating'], data['price']))
            else:
                movies.append(ThreeDimensionalMovie(data['id'], data['name'], data['generes'], data['rating'], data['price']))

        return movies

