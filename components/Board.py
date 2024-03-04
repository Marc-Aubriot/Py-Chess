import pygame

class Board:

    def __init__(self, board_width, board_height) -> None:
        self.id = "board_one"   # str: uuid?
        self.tiles = "hashmap"  # hashmap: Maptile_name "A1" : content "empty" "white_rook" "piece_id"
        self.img = pygame.transform.scale(pygame.image.load("./assets/chess_board_1.png"), (board_width,board_height))

    # affiche le plateau et les pièces dans une fenêtre de jeu
    def draw(self, display):
        display.blit(self.img, (0,0))

    # récupère une liste des pièces restantes (et leurs coordonnées ?)
    def get_pieces_left(self):
        pass

    # rafraichit les cases du plateau
    def update_board(self):
        pass