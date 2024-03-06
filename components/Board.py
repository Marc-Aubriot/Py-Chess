import pygame
from components.Piece import Piece
from components.HelperModule import HelperModule

class Board:

    def __init__(self, board_id, board_width, board_height, tile_size_unit) -> None:
        self.id = board_id                          # str: uuid?
        self.tile_size = tile_size_unit             # int: px
        self.pieces_list = self.populate_board()    # array[Object*]: contient les Pièces
        self.img = pygame.transform.scale(pygame.image.load("./assets/chess_board_1.png"), (board_width,board_height))
        self.helper = HelperModule(f"board_helper")

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
            Piece("white_rook_2", 3, 0, "H1", self.tile_size, 25),
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

    # dessine un rectangle autour du roi pour indiquer qu'il est en échec
    def draw_king_is_checked(self, display, king):
        #king = self.helper.get_piece_by_id(king_id, self.pieces_list)
        pygame.draw.rect(display, (255, 0, 0), (king.coordinates[0], king.coordinates[1], king.size_unit, king.size_unit), 4)

    # dessine les mouvements de la pièce sur le plateau
    def draw_moves(self, display, piece, pieces_list):
        destinations = piece.get_moveset(pieces_list)

        # affiche les destinations possible récupérées
        for dest in destinations:
            new_x = piece.coordinates[0]+dest[0]*piece.size_unit
            new_y = piece.coordinates[1]+dest[1]*piece.size_unit

            if len(dest)>2 and dest[2] == True:
                pygame.draw.rect(display, (255, 0, 0), (new_x, new_y, piece.size_unit, piece.size_unit), 4)
            else:
                pygame.draw.rect(display, (0, 255, 0), (new_x, new_y, piece.size_unit, piece.size_unit), 4)

    # vérifie si le move est valide
    def is_move_valid(self, piece, destination):

        # récupère le moveset de la pièce et transforme les coordonnées (0:800) en xy (0:7)
        piece_moveset = piece.get_moveset(self.pieces_list)
        new_destination = (destination[0]*self.tile_size, destination[1]*self.tile_size)

        # affiche les tiles possibles et vérifie que les coordonnées de destinations sont dans les possibilités
        for tile in piece_moveset:
            new_x = piece.coordinates[0]+tile[0]*piece.size_unit
            new_y = piece.coordinates[1]+tile[1]*piece.size_unit

            # si destination = possibilité => le move est possible
            if new_destination[0] == new_x and new_destination[1] == new_y:
                return True

        return False

    # bouge la piece à destination
    def move_piece(self, piece, chess_tile_name):
        piece.update_coordinate(chess_tile_name)
        piece.move_count += 1

    # le joueur prend la pièce cible, update la liste des pièces en jeu
    def take_piece(self, piece_taken):

        # récupère l'index de la pièce à supprimer de la liste
        piece_index = self.helper.get_piece_index_by_id(piece_taken.id, self.pieces_list)
        self.pieces_list.pop(piece_index)

        # supprime les coordonnées de la pièce et empêche la méthode draw
        piece_taken.xy = None
        piece_taken.coordinates = None
        piece_taken.tile_name = None
        piece_taken.piece_on_table = False

    # check si le roi est en échec
    def is_king_checked(self):

        # récupère les coordonnées des 2 rois
        white_king = self.helper.get_piece_by_id("white_king_1", self.pieces_list)
        black_king = self.helper.get_piece_by_id("black_king_1", self.pieces_list)
        white_king_position = white_king.xy
        black_king_position = black_king.xy
        print(f"wk pos: {white_king_position}")
        print(f"bk pos: {black_king_position}")
        # check chaque piece si elle peut bouger sur le roi adverse
        for piece in self.pieces_list:
            destinations = piece.get_moveset(self.pieces_list)

            for dest in destinations:
                x = piece.xy[0] + dest[0]
                y = piece.xy[1] + dest[1]

                if piece.type == 4 and piece.color == 0:
                    print(f"queen dest: [{x},{y}]")
                if piece.color == 1 and white_king_position[0] == x and white_king_position[1] == y:
                    print("white king checked")
                    return "white_king_check"
                elif piece.color == 0 and black_king_position[0] == x and black_king_position[1] == y:
                    print("black king is checked")
                    return "black_king_check"
                
        return "no"