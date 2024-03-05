import pygame

class Board:

    def __init__(self, board_width, board_height, tile_size_unit) -> None:
        self.id = "board_one"   # str: uuid?
        self.tiles = "hashmap"  # hashmap: Maptile_name "A1" : content "empty" "white_rook" "piece_id"
        self.size_unit = tile_size_unit
        self.tiles_coordinates = self.get_tiles_coordinates()   # hashmap: key:"str" value:tupple( x:int, y:int) pygamme coordinates
        self.tiles_xy = self.get_tiles_xy()   # hashmap: key:"str" value:tupple( x:int, y:int)
        self.img = pygame.transform.scale(pygame.image.load("./assets/chess_board_1.png"), (board_width,board_height))

    # dictionary(key: str, value: tupple(x:int, y:int) ): de chaque case du plateau et ses coordonnées pygame
    def get_tiles_coordinates(self):
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
        return hashmap
    
    # dictionary(key: str, value: str ): de chaque case du plateau et son contenu
    def get_tiles_content(self):
        unit = self.size_unit
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

    # dictionary(key: str, value: tupple(x:int, y:int) ): de chaque case du plateau et ses coordonnées x y
    def get_tiles_xy(self):
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
    
    # void: affiche le plateau et les pièces dans une fenêtre de jeu
    def draw(self, display):
        display.blit(self.img, (0,0))

    # récupère une liste des pièces restantes (et leurs coordonnées ?)
    def get_pieces_left(self):
        pass

    # rafraichit les cases du plateau
    def update_board(self):
        pass