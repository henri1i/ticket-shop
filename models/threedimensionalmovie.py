from .movie import Movie

class ThreeDimensionalMovie(Movie):
    TYPE = '3D movie'
    
    def __init__(self, id: int, name: str, generes: str, rating: int, price: float):
        super().__init__(id, name, generes, rating, price)
        self.price += 10

