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
        self.selected = False       # bool: si la pièce est active
        self.move_count = 0         # int: compte les moves 
        self.detect_colision = True     # bool: détecte la colision entre les pièces
        #self.body = pygame.Rect(self.coordinates[0], self.coordinates[1], tile_size_unit, tile_size_unit)   # pygame object
        #self.helper = HelperModule(f"pawn_{id}_helper")
        self.helper = HelperModule("test")

        self.update_coordinate(chess_tile_name)

    # update les 3 types de coordonnées de l'objet Piece
    def update_coordinate(self, chess_tile_name):
        self.tile_name = chess_tile_name
        coordinates = self.helper.tile_name_coordinates_dictionary(self.size_unit)
        self.coordinates = coordinates[chess_tile_name]
        xy = self.helper.tile_name_xy_dictionary()
        self.xy = xy[chess_tile_name]

    # string: charge l'image qui correspond au type et à la couleur de la pièce
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

    # void: dessine la pièce
    def draw(self, display):
        display.blit(self.img, self.coordinates)

    # void: dessine un rectangle qui montre la sélection de la pièce
    def draw_select_icon(self, display):
        pygame.draw.rect(display, (255, 255, 0), (self.coordinates[0], self.coordinates[1], self.size_unit, self.size_unit), 4)

    # void: dessine les mouvements de la pièce sur le plateau
    def draw_moves(self, display, pieces_list):
        destinations = self.get_moves(pieces_list)

        # affiche les destinations possible récupérées
        for dest in destinations:
            new_x = self.coordinates[0]+dest[0]*self.size_unit
            new_y = self.coordinates[1]+dest[1]*self.size_unit
            pygame.draw.rect(display, (0, 255, 0), (new_x, new_y, self.size_unit, self.size_unit), 4)

    # boolean: check si la pièce peut bouger à cette destination
    def check_move(self, pieces_list, coordinates):

        destinations = self.get_moves(pieces_list)

        # pour chaque case de destination on vérifie si le click est dans les coordonnées
        for dest in destinations:
            dest_x = self.coordinates[0]+dest[0]*self.size_unit
            dest_y = self.coordinates[1]+dest[1]*self.size_unit

            if coordinates[1] >= dest_y and coordinates[1] <=  dest_y + self.size_unit and coordinates[0] >= dest_x and coordinates[0] <= dest_x + self.size_unit:
                return True
        
        return False

    # void: bouge la pièce à sa destination
    def move(self, coordinates):
        coordinates = self.translate_xy_to_piece_coordinates(coordinates)
        self.coordinates = coordinates

    # tupple( x:int, y:int): coordonnées de la pièce sur display pygame
    def translate_xy_to_piece_coordinates(self, xy_coordinates):
        dest_x = xy_coordinates[0]*self.size_unit
        dest_y = xy_coordinates[1]*self.size_unit
        return (dest_x, dest_y)
    
    # array[ array[ x:int, y:int]* ]: vérifie les possibilités de mouvements de la pièce
    def get_moves(self, pieces_list):
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
        
    # boolean: check si une pièce se trouve aux coordonnées
    def check_piece_at_coordinates(self, coordinates, pieces_list):
        for piece in pieces_list:
            if piece.coordinates == (coordinates[0], coordinates[1]):  
                if piece.color != self.color:
                    print("capture possible")
            return True

    # array[ array[ x:int, y:int]* ]: récupère le move set d'un pion
    def pawn_moveset(self, pieces_list):
        # white pawn first move
        if self.type == 0 and self.color == 0 and self.move_count == 0:
            moves = [ [0,-1], [0,-2] ]
        # white pawn
        elif self.type == 0 and self.color == 0:
            moves = [ [0,-1] ]
        # black pawn first move
        elif self.type == 0 and self.color == 1 and self.move_count == 0:
            moves = [ [0,1], [0,2] ]
        # black pawn
        elif self.type == 0 and self.color == 1:
            moves = [ [0,1] ]
        
        return moves
    
    # array[ array[ x:int, y:int]* ]: récupère le move set d'un cavalier
    def knight_moveset(self, pieces_list):
        return [ [-1, -2], [1, -2], [-1, 2], [1, 2], [-2, -1], [-2, 1], [2, -1], [2, 1] ]
    
    # array[ array[ x:int, y:int]* ]: récupère le move set d'un fou
    def bishop_moveset(self, pieces_list):
        moves = []

        # white bishop and black bishop, and white queen and black queen for diagonal moves
        if self.type == 2 or self.type == 4:
            vector = [ [-1, -1], [1, -1], [-1, 1], [1, 1]]
            
            for i in range(4):
                x = self.coordinates[0]/self.size_unit
                y = self.coordinates[1]/self.size_unit
                loop = True
                vX = 0
                vY = 0

                # calculte les destinations tant qu'on est dans le plateau
                while(loop):

                    # ajuste les coordonnées avec le vecteur
                    x = x + vector[i][0]
                    y = y + vector[i][1]

                    # check si la case est occupée par une pièce
                    new_x = x * self.size_unit
                    new_y = y * self.size_unit
                    if self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == True:
                            loop = False
                            continue

                    # quand x ou y arrive au bord du plateau stop cette loop
                    if x < 0 or y < 0 or x >= 8 or y >= 8:
                        loop = False

                    # augmente la distance parcourue à chaque loop
                    elif loop == True:
                        vX = vX + vector[i][0]
                        vY = vY + vector[i][1]
                        moves.append([ vX, vY ])

        return moves

    # array[ array[ x:int, y:int]* ]: récupère le move set d'une tour
    def rook_moveset(self, pieces_list):
        moves = []

        # white rook and black rook, and white queen and black queen for vertical and horizontal moves
        if self.type == 3 or self.type == 4:
            vector = [ [-1, 0], [0, -1], [1, 0], [0, 1]]
            
            for i in range(4):
                x = self.coordinates[0]/self.size_unit
                y = self.coordinates[1]/self.size_unit
                loop = True
                vX = 0
                vY = 0

                # calculte les destinations tant qu'on est dans le plateau
                while(loop):

                    # ajuste les coordonnées avec le vecteur
                    x = x + vector[i][0]
                    y = y + vector[i][1]

                    # check si la case est occupée par une pièce
                    new_x = x * self.size_unit
                    new_y = y * self.size_unit
                    if self.check_piece_at_coordinates( (new_x, new_y), pieces_list) == True:
                            loop = False
                            continue

                    # quand x ou y arrive au bord du plateau stop cette loop
                    if x < 0 or y < 0 or x >= 8 or y >= 8:
                        loop = False

                    # augmente la distance parcourue à chaque loop
                    elif loop == True:
                        vX = vX + vector[i][0]
                        vY = vY + vector[i][1]
                        moves.append([ vX, vY ])

        return moves
    
    # array[ array[ x:int, y:int]* ]: récupère le move set d'une reine
    def queen_moveset(self, pieces_list):
        moves_1 = self.bishop_moveset(pieces_list)
        moves_2 = self.rook_moveset(pieces_list)
        moves = moves_1 + moves_2
        return moves
    
    # array[ array[ x:int, y:int]* ]: récupère le move set d'un roi
    def king_moveset(self, piece_list):
        moves = []
        
        # white king and black king
        if self.type == 5:
            moves = [ [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1] ]

        return moves
        pass