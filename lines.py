class Game:
    def __init__(self):
        self.points = 0

    def won(self):
        self.points += 1

    def lose(self):
        self.points -= 1

    def result(self):
        point = self.points
        return point
