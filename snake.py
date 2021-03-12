# Create Snakes

class Snakes:
    def __init__(self, name, head, tail):
        self.name = name
        self.head = head
        self.tail = tail

    def __repr__(self):
        return Snakes(self.name, self.head, self.tail)

    def __str__(self):
        return f"\nSnake Name : {self.name} \nSnake Head : {self.head} \nSnake Tail : {self.tail}"
