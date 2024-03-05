import pygame
from components.Piece import Piece

class Board:

    def __init__(self, board_id, board_width, board_height, tile_size_unit) -> None:
        self.id = board_id                          # str: uuid?
        self.tile_size = tile_size_unit             # int: px
        self.board = self.board_content()           # hashmap: key:STRING value:STRING
        self.pieces_list = self.populate_board()    # array[Object*]: contient les Pièces
        self.img = pygame.transform.scale(pygame.image.load("./assets/chess_board_1.png"), (board_width,board_height))

    # dictionary(key: str, value: str ): de chaque case du plateau et son contenu
    def board_content(self):
        hashmap = {
            # Y0
            "A8": "empty",
            "B8": "empty",
            "C8": "empty",
            "D8": "empty",
            "E8": "empty",
            "F8": "empty",
            "G8": "empty",
            "H8": "empty",
            # Y1
            "A7": "empty",
            "B7": "empty",
            "C7": "empty",
            "D7": "empty",
            "E7": "empty",
            "F7": "empty",
            "G7": "empty",
            "H7": "empty",
            # Y2
            "A6": "empty",
            "B6": "empty",
            "C6": "empty",
            "D6": "empty",
            "E6": "empty",
            "F6": "empty",
            "G6": "empty",
            "H6": "empty",
            # Y3
            "A5": "empty",
            "B5": "empty",
            "C5": "empty",
            "D5": "empty",
            "E5": "empty",
            "F5": "empty",
            "G5": "empty",
            "H5": "empty",
            # Y4
            "A4": "empty",
            "B4": "empty",
            "C4": "empty",
            "D4": "empty",
            "E4": "empty",
            "F4": "empty",
            "G4": "empty",
            "H4": "empty",
            # Y5
            "A3": "empty",
            "B3": "empty",
            "C3": "empty",
            "D3": "empty",
            "E3": "empty",
            "F3": "empty",
            "G3": "empty",
            "H3": "empty",
            # Y6
            "A2": "empty",
            "B2": "empty",
            "C2": "empty",
            "D2": "empty",
            "E2": "empty",
            "F2": "empty",
            "G2": "empty",
            "H2": "empty",
            # Y7
            "A1": "empty",
            "B1": "empty",
            "C1": "empty",
            "D1": "empty",
            "E1": "empty",
            "F1": "empty",
            "G1": "empty",
            "H1": "empty",
        }
        return hashmap

    # place les pièces sur le plateau de jeu
    def populate_board(self):
        pieces = [
            # id, type, color, chess_tile_name, unit_size(px), index
            # white pawns
            Piece("white_pawn_1", 0, 0, "A2", self.tile_size, 0),
            Piece("white_pawn_2", 0, 0, "B2", self.tile_size, 1),
            Piece("white_pawn_3", 0, 0, "C2", self.tile_size, 2),
            Piece("white_pawn_4", 0, 0, "D2", self.tile_size, 3),
            Piece("white_pawn_5", 0, 0, "E2", self.tile_size, 4),
            Piece("white_pawn_6", 0, 0, "F2", self.tile_size, 5),
            Piece("white_pawn_7", 0, 0, "G2", self.tile_size, 6),
            Piece("white_pawn_8", 0, 0, "H2", self.tile_size, 7),
            # black pawns
            Piece("black_pawn_1", 0, 1, "A7", self.tile_size, 8),
            Piece("black_pawn_2", 0, 1, "B7", self.tile_size, 9),
            Piece("black_pawn_3", 0, 1, "C7", self.tile_size, 10),
            Piece("black_pawn_4", 0, 1, "D7", self.tile_size, 11),
            Piece("black_pawn_5", 0, 1, "E7", self.tile_size, 12),
            Piece("black_pawn_6", 0, 1, "F7", self.tile_size, 13),
            Piece("black_pawn_7", 0, 1, "G7", self.tile_size, 14),
            Piece("black_pawn_8", 0, 1, "H7", self.tile_size, 15),
            # white knight
            Piece("white_knight_1", 1, 0, "B1", self.tile_size, 16),
            Piece("white_knight_2", 1, 0, "G1", self.tile_size, 17),
            # black knight
            Piece("black_knight_1", 1, 1, "B8", self.tile_size, 18),
            Piece("black_knight_2", 1, 1, "G8", self.tile_size, 19),
            # white bishop
            Piece("white_bishop_1", 2, 0, "C1", self.tile_size, 20),
            Piece("white_bishop_2", 2, 0, "F1", self.tile_size, 21),
            # black bishop
            Piece("black_bishop_1", 2, 1, "C8", self.tile_size, 22),
            Piece("black_bishop_2", 2, 1, "F8", self.tile_size, 23),
            # white rook
            Piece("white_rook_1", 3, 0, "A1", self.tile_size, 24),
            Piece("white_rook_1", 3, 0, "H1", self.tile_size, 25),
            # black rook
            Piece("black_rook_1", 3, 1, "A8", self.tile_size, 26),
            Piece("black_rook_2", 3, 1, "H8", self.tile_size, 27),
            # white queen
            Piece("white_queen_1", 4, 0, "D1", self.tile_size, 28),
            # black queen
            Piece("black_queen_1", 4, 1, "D8", self.tile_size, 29),
            # white king
            Piece("white_king_1", 5, 0, "E1", self.tile_size, 30),
            # black king
            Piece("black_king_1", 5, 1, "E8", self.tile_size, 31),
        ]
        return pieces

    # dessine le plateau
    def draw(self, display):
        display.blit(self.img, (0,0))

    # retourne la piece dans la case de l'event
    def get_piece(self, event):
        x, y = event[0], event[1]

        # cherche les coordonnées du click dans les pièces
        for piece in self.pieces_list:

            # créé un body à partir de l'image blit pour détecté la collision
            piece_body = piece.img.get_rect(topleft=(piece.coordinates[0], piece.coordinates[1]))

            # x,y dans le body de la pièce => collision => sélectionne la pièce
            if piece_body.collidepoint(x, y):
                return piece
    
    # dessine un rectangle qui montre la sélection de la pièce
    def draw_select_icon(self, display, piece):
        pygame.draw.rect(display, (255, 255, 0), (piece.coordinates[0], piece.coordinates[1], piece.size_unit, piece.size_unit), 4)

    # dessine les mouvements de la pièce sur le plateau
    def draw_moves(self, display, piece, pieces_list):
        destinations = piece.get_moveset(pieces_list)

        # affiche les destinations possible récupérées
        for dest in destinations:
            new_x = piece.coordinates[0]+dest[0]*piece.size_unit
            new_y = piece.coordinates[1]+dest[1]*piece.size_unit
            pygame.draw.rect(display, (0, 255, 0), (new_x, new_y, piece.size_unit, piece.size_unit), 4)