import pygame 
from pygame import  *
from components.Board import Board
from components.Player import Player
from components.Piece import Piece

class Game:

    def __init__(self) -> None:
        # game var
        self.id = "game_one"                        # str: uuid?
        self.width = 800
        self.height = 800
        self.tile_size = self.width/8
        self.board = Board(self.width, self.height)                # object
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
        pieces = [
            # white pawns
            Piece("white_pawn_1", 0, 0, "A2", self.tile_size),
            Piece("white_pawn_2", 0, 0, "B2", self.tile_size),
            Piece("white_pawn_3", 0, 0, "C2", self.tile_size),
            Piece("white_pawn_4", 0, 0, "D2", self.tile_size),
            Piece("white_pawn_5", 0, 0, "E2", self.tile_size),
            Piece("white_pawn_6", 0, 0, "F2", self.tile_size),
            Piece("white_pawn_7", 0, 0, "G2", self.tile_size),
            Piece("white_pawn_8", 0, 0, "H2", self.tile_size),
            # black pawns
            Piece("black_pawn_1", 0, 1, "A7", self.tile_size),
            Piece("black_pawn_2", 0, 1, "B7", self.tile_size),
            Piece("black_pawn_3", 0, 1, "C7", self.tile_size),
            Piece("black_pawn_4", 0, 1, "D7", self.tile_size),
            Piece("black_pawn_5", 0, 1, "E7", self.tile_size),
            Piece("black_pawn_6", 0, 1, "F7", self.tile_size),
            Piece("black_pawn_7", 0, 1, "G7", self.tile_size),
            Piece("black_pawn_8", 0, 1, "H7", self.tile_size),
            # white knight
            Piece("white_knight_1", 1, 0, "B1", self.tile_size),
            Piece("white_knight_2", 1, 0, "G1", self.tile_size),
            # black knight
            Piece("black_knight_1", 1, 1, "B8", self.tile_size),
            Piece("black_knight_2", 1, 1, "G8", self.tile_size),
            # white bishop
            Piece("white_bishop_1", 2, 0, "C1", self.tile_size),
            Piece("white_bishop_2", 2, 0, "F1", self.tile_size),
            # black bishop
            Piece("black_bishop_1", 2, 1, "C8", self.tile_size),
            Piece("black_bishop_2", 2, 1, "F8", self.tile_size),
            # white rook
            Piece("white_rook_1", 3, 0, "A1", self.tile_size),
            Piece("white_rook_1", 3, 0, "H1", self.tile_size),
            # black rook
            Piece("black_rook_1", 3, 1, "A8", self.tile_size),
            Piece("black_rook_2", 3, 1, "H8", self.tile_size),
            # white queen
            Piece("white_queen_1", 4, 0, "D1", self.tile_size),
            # black queen
            Piece("black_queen_1", 4, 1, "D8", self.tile_size),
            # white king
            Piece("white_king_1", 5, 0, "E1", self.tile_size),
            # black king
            Piece("black_king_1", 5, 1, "E8", self.tile_size),
        ]
        return pieces

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
            
            # click souris
            if event.type == pygame.MOUSEBUTTONDOWN:

                # left click
                if pygame.mouse.get_pressed()[0]:
                    x, y = event.pos
                    for piece in self.pieces:
                        if piece.img.get_rect(topleft=(piece.coordinates[0], piece.coordinates[1])).collidepoint(x, y):
                            print(piece.id)
                            print(f'Mouse clicked at {x}, {y}')
                            piece.selected = True
                            print(piece.selected)
 

                # right click
                elif pygame.mouse.get_pressed()[2]:
                    print("right click")

    # dessine le jeu
    def render(self):
        pygame.display.flip()                                           # Refresh on-screen display
        self.display.fill(pygame.Color(255,255,255))                    # clear surface
        self.clock.tick(15)                                             # wait until next frame

        # dessine le plateau et les pièces
        self.board.draw(self.display)
        for piece in self.pieces:
            piece.draw(self.display)

            # si une pièce est selectionnée, place un curseur jaune sur la case
            if piece.selected == True:
                piece.draw_select_icon(self.display)
            