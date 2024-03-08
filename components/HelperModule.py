import math

class HelperModule:

    def __init__(self, id) -> None:
        self.id = id   # str: uuid ?

    # récupère la Pièce dans une liste de Pièce grâce à son ID
    # INPUT =   STRING: id, ARRAY[OBJECT*]: piece list
    # OUTPUT =  OBJECT: Piece
    def get_piece_by_id(self, piece_id, piece_list):
        for piece in piece_list:
            if piece.id == piece_id:
                return piece
        return None
    
    # récupère la Pièce dans une liste de Pièce grâce à son ID
    # INPUT =   STRING: id, ARRAY[OBJECT*]: piece list
    # OUTPUT =  INT: index dans la liste
    def get_piece_index_by_id(self, piece_id, piece_list):
        index = 0
        for piece in piece_list:
            if piece.id == piece_id:
                return index
            index += 1
        return None
    
    # récupère les coordonnées de la case du jeu d'échec "A1" "B1" etc
    # INPUT =   TUPPLE(INT,INT): coordonnées en px à partir d'un event click, INT: taille d'une unité en px
    # OUTPUT =  STRING: tile_name
    def get_tile_name(self, coordinates, tile_size):
        xy_coordinates = self.get_xy(coordinates, tile_size)
        for key, value in self.tile_name_xy_dictionary().items():
            if value == xy_coordinates:
                return key
        return None

    # récupère les coordonnées de la case du plateau d'échec en format x y / size unit
    # INPUT =   TUPPLE(INT,INT): coordonnées en px à partir d'un event click, INT: taille d'une unité en px
    # OUTPUT =  TUPPLE(INT,INT): coordonnées de case (x,y) en unit 
    def get_xy(self, coordinates, tile_size, left_gutter=0):
        x = math.floor((coordinates[0]+left_gutter)/tile_size)
        y = math.floor((coordinates[1]+left_gutter)/tile_size)
        return (x, y)

    # dictionnaire key value contenant le noms des cases du jeu ("A1" etc) et leurs coordonnées x, y
    # INPUT =   NONE
    # OUTPUT =  DICTIONARY( STRING, TUPPLE(INT,INT) ): A1 => 0,7
    def tile_name_xy_dictionary(self):
        hashmap = {
            # Y0
            "A8": (0,0),
            "B8": (1,0),
            "C8": (2,0),
            "D8": (3,0),
            "E8": (4,0),
            "F8": (5,0),
            "G8": (6,0),
            "H8": (7,0),
            # Y1
            "A7": (0,1),
            "B7": (1,1),
            "C7": (2,1),
            "D7": (3,1),
            "E7": (4,1),
            "F7": (5,1),
            "G7": (6,1),
            "H7": (7,1),
            # Y2
            "A6": (0,2),
            "B6": (1,2),
            "C6": (2,2),
            "D6": (3,2),
            "E6": (4,2),
            "F6": (5,2),
            "G6": (6,2),
            "H6": (7,2),
            # Y3
            "A5": (0,3),
            "B5": (1,3),
            "C5": (2,3),
            "D5": (3,3),
            "E5": (4,3),
            "F5": (5,3),
            "G5": (6,3),
            "H5": (7,3),
            # Y4
            "A4": (0,4),
            "B4": (1,4),
            "C4": (2,4),
            "D4": (3,4),
            "E4": (4,4),
            "F4": (5,4),
            "G4": (6,4),
            "H4": (7,4),
            # Y5
            "A3": (0,5),
            "B3": (1,5),
            "C3": (2,5),
            "D3": (3,5),
            "E3": (4,5),
            "F3": (5,5),
            "G3": (6,5),
            "H3": (7,5),
            # Y6
            "A2": (0,6),
            "B2": (1,6),
            "C2": (2,6),
            "D2": (3,6),
            "E2": (4,6),
            "F2": (5,6),
            "G2": (6,6),
            "H2": (7,6),
            # Y7
            "A1": (0,7),
            "B1": (1,7),
            "C1": (2,7),
            "D1": (3,7),
            "E1": (4,7),
            "F1": (5,7),
            "G1": (6,7),
            "H1": (7,7)
        }
        return hashmap
    
    # dictionnaire key value contenant le noms des cases du jeu ("A1" etc) et les coordonnées display
    # INPUT =   INT: taille des cases du plateau en px
    # OUTPUT =  DICTIONARY( STRING, TUPPLE(INT,INT) ): A1 => 0,800
    def tile_name_coordinates_dictionary(self, size_unit, left_gutter=0):
        unit = size_unit
        hashmap = {
            # Y0
            "A8": (0*unit+left_gutter,0*unit),
            "B8": (1*unit+left_gutter,0*unit),
            "C8": (2*unit+left_gutter,0*unit),
            "D8": (3*unit+left_gutter,0*unit),
            "E8": (4*unit+left_gutter,0*unit),
            "F8": (5*unit+left_gutter,0*unit),
            "G8": (6*unit+left_gutter,0*unit),
            "H8": (7*unit+left_gutter,0*unit),
            # Y1
            "A7": (0*unit+left_gutter,1*unit),
            "B7": (1*unit+left_gutter,1*unit),
            "C7": (2*unit+left_gutter,1*unit),
            "D7": (3*unit+left_gutter,1*unit),
            "E7": (4*unit+left_gutter,1*unit),
            "F7": (5*unit+left_gutter,1*unit),
            "G7": (6*unit+left_gutter,1*unit),
            "H7": (7*unit+left_gutter,1*unit),
            # Y2
            "A6": (0*unit+left_gutter,2*unit),
            "B6": (1*unit+left_gutter,2*unit),
            "C6": (2*unit+left_gutter,2*unit),
            "D6": (3*unit+left_gutter,2*unit),
            "E6": (4*unit+left_gutter,2*unit),
            "F6": (5*unit+left_gutter,2*unit),
            "G6": (6*unit+left_gutter,2*unit),
            "H6": (7*unit+left_gutter,2*unit),
            # Y3
            "A5": (0*unit+left_gutter,3*unit),
            "B5": (1*unit+left_gutter,3*unit),
            "C5": (2*unit+left_gutter,3*unit),
            "D5": (3*unit+left_gutter,3*unit),
            "E5": (4*unit+left_gutter,3*unit),
            "F5": (5*unit+left_gutter,3*unit),
            "G5": (6*unit+left_gutter,3*unit),
            "H5": (7*unit+left_gutter,3*unit),
            # Y4
            "A4": (0*unit+left_gutter,4*unit),
            "B4": (1*unit+left_gutter,4*unit),
            "C4": (2*unit+left_gutter,4*unit),
            "D4": (3*unit+left_gutter,4*unit),
            "E4": (4*unit+left_gutter,4*unit),
            "F4": (5*unit+left_gutter,4*unit),
            "G4": (6*unit+left_gutter,4*unit),
            "H4": (7*unit+left_gutter,4*unit),
            # Y5
            "A3": (0*unit+left_gutter,5*unit),
            "B3": (1*unit+left_gutter,5*unit),
            "C3": (2*unit+left_gutter,5*unit),
            "D3": (3*unit+left_gutter,5*unit),
            "E3": (4*unit+left_gutter,5*unit),
            "F3": (5*unit+left_gutter,5*unit),
            "G3": (6*unit+left_gutter,5*unit),
            "H3": (7*unit+left_gutter,5*unit),
            # Y6
            "A2": (0*unit+left_gutter,6*unit),
            "B2": (1*unit+left_gutter,6*unit),
            "C2": (2*unit+left_gutter,6*unit),
            "D2": (3*unit+left_gutter,6*unit),
            "E2": (4*unit+left_gutter,6*unit),
            "F2": (5*unit+left_gutter,6*unit),
            "G2": (6*unit+left_gutter,6*unit),
            "H2": (7*unit+left_gutter,6*unit),
            # Y7
            "A1": (0*unit+left_gutter,7*unit),
            "B1": (1*unit+left_gutter,7*unit),
            "C1": (2*unit+left_gutter,7*unit),
            "D1": (3*unit+left_gutter,7*unit),
            "E1": (4*unit+left_gutter,7*unit),
            "F1": (5*unit+left_gutter,7*unit),
            "G1": (6*unit+left_gutter,7*unit),
            "H1": (7*unit+left_gutter,7*unit)
        }
        return hashmap
