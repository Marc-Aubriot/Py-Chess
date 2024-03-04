import pygame

class Piece:

    def __init__(self, id, type, color, chess_coordinates, tile_size_unit) -> None:
        self.id = id                                                    # str: uuid ?
        self.type = type                                                # int: 0 pawn, 1 knight, 2 bishop, 3 rook, 4 queen, 5 king
        self.color = color                                              # int: 0 blanc, 1 noir
        self.coordinates = self.get_coordinates(chess_coordinates, tile_size_unit)      # tupple[int,int] : [x,y]
        self.img = pygame.transform.scale(pygame.image.load(self.get_image()), (85,85))                  # method: load the correct img
        print(self.coordinates)

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

    # récupère les coordonnées tupple: (x,y) via hashmap avec les coordoonées du plateau string: "A1", "B2", etc
    def get_coordinates(self, chess_coordinates, tile_size_unit):
        unit = tile_size_unit
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

    # dessine la pièce
    def draw(self, display):
        display.blit(self.img, self.coordinates)

    # bouge la pièce à une destination
    def move(self):
        pass

    # vérifie les possibilités de mouvements de la pièce
    def check_move(self):
        pass

    # transforme un pion en une autre pièce
    def upgrade_pawn(self):
        pass