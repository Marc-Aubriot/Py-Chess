import pygame
from components.HelperModule import HelperModule

class Piece:

    def __init__(self, id, type, color, chess_tile_name, tile_size_unit, pieces_list_index) -> None:
        self.id = id                # str: uuid ?
        self.type = type            # int: 0 pawn, 1 knight, 2 bishop, 3 rook, 4 queen, 5 king
        self.color = color          # int: 0 blanc, 1 noir
        self.size_unit = tile_size_unit # int: la taille en px du carré représentant l'objet
        self.piece_list_index = pieces_list_index   # int:  son index dans la liste des pieces de Game
        self.coordinates = None          # tupple[int,int] : [x,y]
        self.xy =   None
        self.tile_name = None
        self.img = pygame.transform.scale(pygame.image.load(self.get_image()), (85,85))     # method: load the correct img
        self.move_count = 0        # int: compte les moves 
        #self.detect_colision = True     # bool: détecte la colision entre les pièces
        self.helper = HelperModule(f"pawn_{id}_helper")
        self.piece_on_table = True
        self.piece_is_checked = False

        self.update_coordinate(chess_tile_name)

    # update les 3 types de coordonnées de l'objet Piece
    def update_coordinate(self, chess_tile_name):
        self.tile_name = chess_tile_name
        coordinates = self.helper.tile_name_coordinates_dictionary(self.size_unit)
        self.coordinates = coordinates[chess_tile_name]
        xy = self.helper.tile_name_xy_dictionary()
        self.xy = xy[chess_tile_name]

    # charge l'image qui correspond au type et à la couleur de la pièce
    def get_image(self):
        img = ""
        if self.color == 0:
            img = "w"
        else:
            img = "b"

        match self.type:
            case 0:
                img += "_pawn"
            case 1:
                img += "_knight"
            case 2:
                img += "_bishop"
            case 3:
                img += "_rook"
            case 4:
                img += "_queen"
            case 5:
                img += "_king"
            case _:
                print("Piece has no type")

        return "./assets/"+img+".png"

    # dessine la pièce
    def draw(self, display):
        if self.piece_on_table == True:
            display.blit(self.img, self.coordinates)

    # vérifie les possibilités de mouvements de la pièce
    def get_moveset(self, pieces_list):
        moves = []

        # pawn piece
        if self.type == 0:
            moves = self.pawn_moveset(pieces_list)

        # white knight and black knight
        if self.type == 1:
            moves = self.knight_moveset(pieces_list)

        # white bishop and black bishop
        if self.type == 2:
            moves = self.bishop_moveset(pieces_list)

        # white rook and black rook
        if self.type == 3:
            moves = self.rook_moveset(pieces_list)

        # white queen and black queen
        if self.type == 4:
            moves = self.queen_moveset(pieces_list)

        # white king and black king
        if self.type == 5:
            moves = self.king_moveset(pieces_list)
        
        return moves
        
    # check si une pièce se trouve aux coordonnées
    def check_piece_at_coordinates(self, coordinates, pieces_list):
        for piece in pieces_list:
            if piece.coordinates == (coordinates[0], coordinates[1]):

                # piece adverse
                if self.color != piece.color:
                    return "capture"  
                
                return True
            
        return False

    # récupère le move set d'un pion
    def pawn_moveset(self, pieces_list):
        moves = []

        # pawn only
        if self.type != 0:
            return

        for i in range(3):

            # les moves en fonction du tour et de la couleur
            if self.color == 0 and self.move_count == 0:
                vectors = [ [-1, -1], [0,-1], [1, -1], [0, -2] ]
            elif self.color == 1 and self.move_count == 0:
                vectors = [ [-1, 1], [0,1], [1, 1], [0, 2] ]
            elif self.color == 0 and self.move_count != 0:
                vectors = [ [-1, -1], [0,-1], [1, -1] ]
            elif self.color == 1 and self.move_count != 0:
                vectors = [ [-1, 1], [0,1], [1, 1] ]

            x = self.xy[0] + vectors[i][0]
            y = self.xy[1] + vectors[i][1]

            # check si la case est occupée par une pièce, sinon append le move
            new_x = x * self.size_unit
            new_y = y * self.size_unit

            # pion sur case de gauche => prise
            if i == 0 and self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == "capture":
                moves.append([ vectors[i][0], vectors[i][1], True ])
                continue
            
            # pion sur case devant => piece n'avance pas
            elif i == 1 and self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == "capture":
                continue
            
            # case devant libre => piece avance
            elif i == 1 and self.check_piece_at_coordinates( (new_x, new_y), pieces_list) != True:
                moves.append([ vectors[i][0], vectors[i][1] ])

                # premier tour du pion, deuxieme case devant libre => piece avance 2 cases
                if self.move_count == 0 and self.check_piece_at_coordinates( (new_x, new_y), pieces_list) != True:
                    moves.append([ vectors[3][0], vectors[3][1] ])

            # pion sur case de droite => prise
            elif i == 2 and self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == "capture":
                moves.append([ vectors[i][0], vectors[i][1], True ])
                continue

        return moves
    
    # récupère le move set d'un cavalier
    def knight_moveset(self, pieces_list):
        moves = []

        # knight only
        if self.type != 1:
            return

        vectors = [ [-1, -2], [1, -2], [-1, 2], [1, 2], [-2, -1], [-2, 1], [2, -1], [2, 1] ]

        for i in range(len(vectors)):

            # ajuste les coordonnées avec le vecteur
            x = self.xy[0] + vectors[i][0]
            y = self.xy[1] + vectors[i][1]

            # check les bords du plateau
            if x < 0 or x > 7 or y < 0 or y > 7:
                continue

            # check si la case est occupée par une pièce, sinon append le move
            new_x = x * self.size_unit
            new_y = y * self.size_unit

            if self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == True:
                continue
            elif self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == "capture": 
                moves.append([ vectors[i][0], vectors[i][1], True ])
                continue

            moves.append([ vectors[i][0], vectors[i][1] ])

        return moves
    
    # récupère le move set d'un fou
    def bishop_moveset(self, pieces_list):
        moves = []

        # white bishop and black bishop, and white queen and black queen for diagonal moves
        if self.type == 2 or self.type == 4:
            vector = [ [-1, -1], [1, -1], [-1, 1], [1, 1]]
            
            for i in range(4):
                x = self.xy[0]
                y = self.xy[1]
                loop = True
                vX = 0
                vY = 0
                enemy_piece_can_be_taken = False

                # calculte les destinations tant qu'on est dans le plateau
                while(loop):

                    # fin du move dans cette trajectoire
                    if enemy_piece_can_be_taken == True:
                        loop = False
                        continue

                    # ajuste les coordonnées avec le vecteur
                    x = x + vector[i][0]
                    y = y + vector[i][1]

                    # check si la case est occupée par une pièce, si pièce enenmie lève un flag de capture
                    new_x = x * self.size_unit
                    new_y = y * self.size_unit
                    if self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == True:
                        loop = False
                        continue
                    elif self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == "capture": 
                        enemy_piece_can_be_taken = True

                    # quand x ou y arrive au bord du plateau stop cette loop
                    if x < 0 or y < 0 or x > 7 or y > 7:
                        loop = False

                    # augmente la distance parcourue à chaque loop
                    elif loop == True:
                        vX = vX + vector[i][0]
                        vY = vY + vector[i][1]
                        if enemy_piece_can_be_taken == True:
                            moves.append([ vX, vY, True ])
                        else:
                            moves.append([ vX, vY ])

        return moves

    # récupère le move set d'une tour
    def rook_moveset(self, pieces_list):
        moves = []

        # white rook and black rook, and white queen and black queen for vertical and horizontal moves
        if self.type == 3 or self.type == 4:
            vector = [ [-1, 0], [0, -1], [1, 0], [0, 1]]
            
            for i in range(4):
                x = self.xy[0]
                y = self.xy[1]
                loop = True
                vX = 0
                vY = 0
                enemy_piece_can_be_taken = False

                # calculte les destinations tant qu'on est dans le plateau
                while(loop):

                    # fin du move dans cette trajectoire
                    if enemy_piece_can_be_taken == True:
                        loop = False
                        continue

                    # ajuste les coordonnées avec le vecteur
                    x = x + vector[i][0]
                    y = y + vector[i][1]

                    # check si la case est occupée par une pièce
                    new_x = x * self.size_unit
                    new_y = y * self.size_unit
                    if self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == True:
                        loop = False
                        continue
                    elif self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == "capture": 
                        enemy_piece_can_be_taken = True

                    # quand x ou y arrive au bord du plateau stop cette loop
                    if x < 0 or y < 0 or x > 7 or y > 7:
                        loop = False

                    # augmente la distance parcourue à chaque loop
                    elif loop == True:
                        vX = vX + vector[i][0]
                        vY = vY + vector[i][1]
                        if enemy_piece_can_be_taken == True:
                            moves.append([ vX, vY, True ])
                        else:
                            moves.append([ vX, vY ])

        return moves
    
    # récupère le move set d'une reine
    def queen_moveset(self, pieces_list):
        moves_1 = self.bishop_moveset(pieces_list)
        moves_2 = self.rook_moveset(pieces_list)
        moves = moves_1 + moves_2
        return moves
    
    # récupère le move set d'un roi
    def king_moveset(self, pieces_list):
        moves = []
        
        # white king and black king
        if self.type != 5:
            return

        vectors = [ [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1] ]

        for i in range(len(vectors)):
            
            # ajuste les coordonnées avec le vecteur
            x = self.xy[0] + vectors[i][0]
            y = self.xy[1] + vectors[i][1]

            # check les bords du plateau
            if x < 0 or x > 7 or y < 0 or y > 7:
                continue

            # check si la case est occupée par une pièce, sinon append le move
            new_x = x * self.size_unit
            new_y = y * self.size_unit

            if self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == True:
                continue
            elif self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == "capture": 
                moves.append([ vectors[i][0], vectors[i][1], True ])
                continue
           
            moves.append([ vectors[i][0], vectors[i][1] ])

        return moves
