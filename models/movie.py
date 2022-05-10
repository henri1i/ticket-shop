class Movie:
    TYPE = 'Regular movie'
    
    def __init__(self, id: int, name: str, generes: str, rating: int, price: float):
        self.id = id
        self.name = name
        self.generes = generes
        self.price = price
        self.setRating(rating)

    def setRating(self, rating: int):
        if (rating < 0 or rating > 10):
            raise Exception("Invalid rating value")

        self.__rating = rating

    def getRating(self):
        return self.__rating

