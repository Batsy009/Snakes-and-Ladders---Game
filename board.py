# Create Board

class Board:
    def __init__(self, bs, bl, size=100):
        self.size = size
        self.bs = bs  # snakes on board
        self.bl = bl  # ladders on board

    def __str__(self):
        return self.size
