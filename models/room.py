from .seat import Seat

class Room:
    def __init__(self, seat: Seat, code: str):
        self.seat = seat
        self.code = code
