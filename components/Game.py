import pygame 
from pygame import  *
from components.Board import Board
from components.Player import Player

class Game:

    def __init__(self) -> None:
        # game var
        self.id = "game_one"                        # str: uuid?
        self.board = Board()                        # object
        self.pieces = self.populate_board()         # array[object*]: contenant les 32 pièces
        #self.players = [Player(0), Player(1)]       # array[object*]: contenant les 2 joueurs
        self.turn_count = 0                         # int: le nombre de tour
        self.active_player = 0                      # int: player_id

        # pygame var
        self.instance = pygame.init()
        self.title = pygame.display.set_caption("Py chess")
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((800,800))

        self.loop = self.main_loop()

    # place les pièces sur le plateau de jeu
    def populate_board(self):
        pass

    # termine la partie
    def game_end(self):
        pass

    # la loop logique du jeu
    def main_loop(self):
        while True:
            # player inputs
            self.inputs()

            # render
            self.render()

    # récupère les inputs du joueur avec pygame
    def inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

    # dessine le jeu
    def render(self):
        pygame.display.flip()                                           # Refresh on-screen display
        self.display.fill(pygame.Color(255,255,255))                    # clear surface
        self.clock.tick(15)                                             # wait until next frame

        self.board.draw(self.display)
        #for piece in self.pieces:
        #    piece.draw()