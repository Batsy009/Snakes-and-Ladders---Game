# Create Ladders

class Ladders:
    def __init__(self, name, head, tail):
        self.name = name
        self.head = head
        self.tail = tail

    def __repr__(self):
        return Ladders(self.name, self.head, self.tail)

    def __str__(self):
        return f"\nLadder Name : {self.name} \nLadder Head : {self.head} \nLadder Tail : {self.tail}"
