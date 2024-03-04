import components.Game as Game

class App:

    def __init__(self) -> None:
        self.game = Game()
        self.game.game_start()