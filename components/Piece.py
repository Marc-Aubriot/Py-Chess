import pygame

class Piece:

    def __init__(self, id, type, color, chess_coordinates, tile_size_unit) -> None:
        self.id = id                # str: uuid ?
        self.type = type            # int: 0 pawn, 1 knight, 2 bishop, 3 rook, 4 queen, 5 king
        self.color = color          # int: 0 blanc, 1 noir
        self.size_unit = tile_size_unit # int: la taille en px du carré représentant l'objet
        self.coordinates = self.get_coordinates(chess_coordinates)          # tupple[int,int] : [x,y]
        self.img = pygame.transform.scale(pygame.image.load(self.get_image()), (85,85))     # method: load the correct img
        self.selected = False       # bool: si la pièce est active
        self.move_count = 0         # int: compte les moves 
        self.detect_colision = True     # bool: détecte la colision entre les pièces
        self.body = pygame.Rect(self.coordinates[0], self.coordinates[1], tile_size_unit, tile_size_unit)   # pygame object

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

    # tupple( x:int, y:int ): récupère les coordonnées de la pièce avec les coordoonées du plateau input: string: "A1", "B2", etc
    def get_coordinates(self, chess_coordinates):
        unit = self.size_unit
        hashmap = {
            # Y0
            "A8": (0*unit,0*unit),
            "B8": (1*unit,0*unit),
            "C8": (2*unit,0*unit),
            "D8": (3*unit,0*unit),
            "E8": (4*unit,0*unit),
            "F8": (5*unit,0*unit),
            "G8": (6*unit,0*unit),
            "H8": (7*unit,0*unit),
            # Y1
            "A7": (0*unit,1*unit),
            "B7": (1*unit,1*unit),
            "C7": (2*unit,1*unit),
            "D7": (3*unit,1*unit),
            "E7": (4*unit,1*unit),
            "F7": (5*unit,1*unit),
            "G7": (6*unit,1*unit),
            "H7": (7*unit,1*unit),
            # Y2
            "A6": (0*unit,2*unit),
            "B6": (1*unit,2*unit),
            "C6": (2*unit,2*unit),
            "D6": (3*unit,2*unit),
            "E6": (4*unit,2*unit),
            "F6": (5*unit,2*unit),
            "G6": (6*unit,2*unit),
            "H6": (7*unit,2*unit),
            # Y3
            "A5": (0*unit,3*unit),
            "B5": (1*unit,3*unit),
            "C5": (2*unit,3*unit),
            "D5": (3*unit,3*unit),
            "E5": (4*unit,3*unit),
            "F5": (5*unit,3*unit),
            "G5": (6*unit,3*unit),
            "H5": (7*unit,3*unit),
            # Y4
            "A4": (0*unit,4*unit),
            "B4": (1*unit,4*unit),
            "C4": (2*unit,4*unit),
            "D4": (3*unit,4*unit),
            "E4": (4*unit,4*unit),
            "F4": (5*unit,4*unit),
            "G4": (6*unit,4*unit),
            "H4": (7*unit,4*unit),
            # Y5
            "A3": (0*unit,5*unit),
            "B3": (1*unit,5*unit),
            "C3": (2*unit,5*unit),
            "D3": (3*unit,5*unit),
            "E3": (4*unit,5*unit),
            "F3": (5*unit,5*unit),
            "G3": (6*unit,5*unit),
            "H3": (7*unit,5*unit),
            # Y6
            "A2": (0*unit,6*unit),
            "B2": (1*unit,6*unit),
            "C2": (2*unit,6*unit),
            "D2": (3*unit,6*unit),
            "E2": (4*unit,6*unit),
            "F2": (5*unit,6*unit),
            "G2": (6*unit,6*unit),
            "H2": (7*unit,6*unit),
            # Y7
            "A1": (0*unit,7*unit),
            "B1": (1*unit,7*unit),
            "C1": (2*unit,7*unit),
            "D1": (3*unit,7*unit),
            "E1": (4*unit,7*unit),
            "F1": (5*unit,7*unit),
            "G1": (6*unit,7*unit),
            "H1": (7*unit,7*unit)
        }
        return hashmap[chess_coordinates]

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

    # tuplle( x:int, y:int): coordonnées de la pièce sur display pygame
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

    # transforme un pion en une autre pièce
    def upgrade_pawn(self):
        pass