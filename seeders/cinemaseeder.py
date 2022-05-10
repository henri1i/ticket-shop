from .faker import Faker
import sys
import requests
sys.path.append("..")
from models.cinema import Cinema
from models.seat import Seat
from models.room import Room

class CinemaSeeder:
    @staticmethod
    def getCinemas(count: int):
        fakeCinemas = Faker.getRandomData(count, 'data/cinemas.json')

        cinemas = []
        for i in range(count):
            currentCinema = fakeCinemas[i]
            seat = Seat(currentCinema['chair_number'])
            room = Room(seat, currentCinema['room_code'])
            cinema = Cinema(currentCinema['cinema_name'], room)
            
            cinemas.append(cinema)

        return cinemas

