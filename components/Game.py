import components.Board as Board
import components.Player as Player

class Game:

    def __init__(self) -> None:
        self.id = None              # str: uuid?
        self.board = None           # object
        self.pieces = None          # array[object*]: contenant les 32 pièces
        self.players = None         # array[object*]: contenant les 2 joueurs
        self.turn_count = None      # int: le nombre de tour
        self.active_player = None   # int: player_id

    # initialise les variables de la partie
    def game_start(self):
        self.id = "game_one"
        self.board = Board()
        self.pieces = self.populate_board()
        self.players = [Player(), Player()]
        self.turn_count = 0

    # place les pièces sur le plateau de jeu
    def populate_board(self):
        pass

    # termine la partie
    def game_end(self):
        pass

    # la loop logique du jeu
    def main_loop(self):
        pass