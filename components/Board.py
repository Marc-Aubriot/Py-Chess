import pygame
from components.Piece import Piece
from components.HelperModule import HelperModule

class Board:

    def __init__(self, board_id, board_width, board_height, tile_size_unit) -> None:
        self.id = board_id                          # STRING
        self.tile_size = tile_size_unit             # INT
        self.pieces_list = self.populate_board()    # ARRAY[OBJECT(Piece)*]
        self.img = pygame.transform.scale(pygame.image.load("./assets/chess_board_1.png"), (board_width,board_height))  # SURFACE
        self.helper = HelperModule(f"board_helper") # objet contenant des méthodes
        self.piece_checking = None                  # OBJECT(Piece)

    # ARRAY[OBJECT(Piece)*]: place les pièces sur le plateau de jeu
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

    # VOID: dessine le plateau
    def draw(self, display):
        display.blit(self.img, (0,0))

    # OBJECT(Piece): retourne la piece dans la case de l'event
    def get_piece(self, event):
        x, y = event[0], event[1]

        # cherche les coordonnées du click dans les pièces
        for piece in self.pieces_list:

            # créé un body à partir de l'image blit pour détecté la collision
            piece_body = piece.img.get_rect(topleft=(piece.coordinates[0], piece.coordinates[1]))

            # x,y dans le body de la pièce => collision => sélectionne la pièce
            if piece_body.collidepoint(x, y):
                return piece

        return None
    
    # VOID: dessine un rectangle qui montre la sélection de la pièce
    def draw_select_icon(self, display, piece):
        pygame.draw.rect(display, (255, 255, 0), (piece.coordinates[0], piece.coordinates[1], piece.size_unit, piece.size_unit), 4)

    # VOID: dessine un rectangle autour du roi pour indiquer qu'il est en échec
    def draw_king_is_checked(self, display, king):
        pygame.draw.rect(display, (255, 0, 0), (king.coordinates[0], king.coordinates[1], king.size_unit, king.size_unit), 4)

    # VOID: dessine les mouvements de la pièce sur le plateau
    def draw_moves(self, display, piece, pieces_list):
        moves_vector = piece.get_moveset(pieces_list)
        destinations = self.get_moves_coordinates(piece, moves_vector)

        # affiche les destinations possible récupérées
        for dest in destinations:

            if len(dest)>2 and dest[2] == True:
                pygame.draw.rect(display, (255, 0, 0), (dest[0], dest[1], piece.size_unit, piece.size_unit), 4)
            else:
                pygame.draw.rect(display, (0, 255, 0), (dest[0], dest[1], piece.size_unit, piece.size_unit), 4)

    # ARRAY[TUPPLE(INT,INT)*]: récupère les cases de déplacements valide pour la pièce
    def get_moves_coordinates(self, piece, moveset):
        destinations = []
        for dest in moveset:
            new_x = piece.coordinates[0]+dest[0]*piece.size_unit
            new_y = piece.coordinates[1]+dest[1]*piece.size_unit
            if len(dest)>2 and dest[2] == True:
                destinations.append([new_x, new_y, True])
            else:
                destinations.append([new_x, new_y])
        return destinations

    # BOOLEAN: vérifie si le move est valide
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

    # BOOLEAN: bouge la pièce vers une case destination
    def move_piece(self, piece_id, destination):

        # récupère la piece active
        active_piece = self.helper.get_piece_by_id(piece_id, self.pieces_list)

        # check si la piece peut bouger à ces coordonnées
        new_destination = self.helper.get_xy(destination, self.tile_size)
        tile_name = self.helper.get_tile_name(destination, self.tile_size)

        if self.is_move_valid(active_piece, new_destination) == True:
            active_piece.update_coordinate(tile_name)
            active_piece.move_count += 1
            return True
        else:
            print("déplacement non permis")
            return False
        
    # BOOLEAN: le joueur prend la pièce cible, update la liste des pièces en jeu
    def take_piece(self, piece_id, destination):

        # récupère la piece active et la pièce cible
        active_piece = self.helper.get_piece_by_id(piece_id, self.pieces_list)
        enemy_piece = self.get_piece(destination)

        # check si la piece peut bouger à ces coordonnées
        new_destination = self.helper.get_xy(destination, self.tile_size)
        tile_name = self.helper.get_tile_name(destination, self.tile_size)

        if self.is_move_valid(active_piece, new_destination) == True:
            active_piece.update_coordinate(tile_name)
            active_piece.move_count += 1

            # récupère l'index de la pièce à supprimer de la liste
            piece_index = self.helper.get_piece_index_by_id(enemy_piece.id, self.pieces_list)
            self.pieces_list.pop(piece_index)

            # supprime les coordonnées de la pièce et empêche la méthode draw
            enemy_piece.xy = None
            enemy_piece.coordinates = None
            enemy_piece.tile_name = None
            enemy_piece.on_table = False
            return True
        else:
            print("déplacement non permis")
            return False

    # STRING: check si le roi est en échec
    def is_king_checked(self):

        # récupère les coordonnées des 2 rois
        white_king = self.helper.get_piece_by_id("white_king_1", self.pieces_list)
        black_king = self.helper.get_piece_by_id("black_king_1", self.pieces_list)
        white_king_position = white_king.xy
        black_king_position = black_king.xy

        # check chaque piece si elle peut bouger sur le roi adverse
        for piece in self.pieces_list:
            destinations = piece.get_moveset(self.pieces_list)

            for dest in destinations:
                x = piece.xy[0] + dest[0]
                y = piece.xy[1] + dest[1]

                # check si la pièce met en échec le king d'un move précédent => annule l'échec temporairement
                if piece.checking_king == True:
                    piece.checking_king = False
                    self.piece_checking = False

                # si roi blanc en échec => garde la pièce et modifie son statut
                elif piece.color == 1 and white_king_position[0] == x and white_king_position[1] == y:
                    piece.checking_king = True
                    self.piece_checking = piece
                    return "white_king_check"
                
                # si roi noir en échec => garde la pièce et modifie son statut
                elif piece.color == 0 and black_king_position[0] == x and black_king_position[1] == y:
                    piece.checking_king = True
                    self.piece_checking = piece
                    return "black_king_check"
                
        return "no"
    
    # BOOLEAN: check si la pièce sélectionner peut empêcher la mise en échec de son roi
    def remove_checked_king(self, piece, king):

        # récupère les moves de la pièce
        piece_vector = piece.get_moveset(self.pieces_list)
        piece_destinations = self.get_moves_coordinates(piece, piece_vector)

        # récupère la pièce qui met échec et son moveset
        enemy_piece_checking = self.piece_checking
        enemy_piece_vector = enemy_piece_checking.get_moveset(self.pieces_list)
        enemy_piece_destinations = self.get_moves_coordinates(enemy_piece_checking, enemy_piece_vector)

        # la pièce sélectionnée peut prendre la pièce ennemie
        for dest in piece_destinations:
            if dest[0] == enemy_piece_checking.coordinates[0] and dest[1] == enemy_piece_checking.coordinates[1]:
                print("test case 0")
                return True

            # pion: il faut bouger le roi 
            if enemy_piece_checking.type == 0 and piece.type == 5:
                print("test case 1")
                return True
        
            # knight: il faut bouger le roi
            if enemy_piece_checking.type == 1 and piece.type == 5:
                print("test case 2")
                return True
        
            # fou: il faut bloquer la trajectoire ou prendre le fou
            if enemy_piece_checking.type == 2 or enemy_piece_checking.type == 4:
                print("test case 3")
                # pour chaque destination on regarde si une destination de la pièce ennemie est la même
                for enemy_dest in enemy_piece_destinations:

                    # si une case est partagé, on vérifie que c'est la même ligne qui met en échec le roi
                    if enemy_dest == dest:
                        print(dest)
                        # on explore chaque vecteur jusqu'à arriver à X ou Y de la pièce ennemie, si on tombe sur la piece ennemie c'est bon
                        vector = [ [-1, -1], [1, -1], [1, 1], [-1, 1]]

                        for i in range(len(vector)):
                            print(i)
                            loop = True
                            x = dest[0]/piece.size_unit
                            y = dest[1]/piece.size_unit
                            print(f"piece original xy = ({x},{y})")
                            target_x = enemy_piece_checking.xy[0]
                            target_y = enemy_piece_checking.xy[1]

                            while(loop):
                                print(i)
                                x = x + vector[i][0]
                                y = y + vector[i][1]
                                print(f"piece new xy with vector = ({x},{y})")
                                # vérifie les limites du plateaua
                                if x > 7 or x < 0 or y > 7 or y < 0:
                                    loop = False
                                    print("out of board")
                                    continue

                                # on tombe sur la pièce ennemie avec ce vecteur
                                if x == target_x and y == target_y:
                                    return True


            # tour: il faut bloquer la trajectoire ou prendre la tour, on se positionne soit sur le même X soit sur même Y
            if enemy_piece_checking.type == 3 or enemy_piece_checking.type == 4:
                print("test case 4")
                # si on peut se mettre sur la même colonne vérifie qu'on se trouve entre le roi et la tour
                if dest[0] == king.xy[0]:
                    print("meme ligne")
                    if king.xy[0] > dest[0] and dest[0] > enemy_piece_checking.xy[0]:
                        return True
                    elif king.xy[0] < dest[0] and dest[0] < enemy_piece_checking.xy[0]:
                        return True
                    
                # si on peut se mettre sur la même ligne vérifie qu'on se trouve entre le roi et la tour
                if dest[1] == king.xy[1]:
                    print("meme colonne")
                    if king.xy[1] > dest[1] and dest[1] > enemy_piece_checking.xy[1]:
                        return True
                    elif king.xy[1] < dest[1] and dest[1] < enemy_piece_checking.xy[1]:
                        return True
                           
        # reine: il faut bloquer la trajectoire ou prendre la reine (get moveset après move de la piece allié)
        return False
    