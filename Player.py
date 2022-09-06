from Ally import Ally


class Player(Ally):
    def __init__(self, x:int, y:int):
        super().__init__(x, y)
        self.color = (0, 125, 125)
        self.xDeslocation = 0

    def run(self, screen, enemys):
        if self.health > 0:
            self.draw(screen)
            self.move()
