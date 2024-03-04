import pygame

class Piece:

    def __init__(self) -> None:
        self.id = "piece_num"   # str: uuid ?
        self.type = 0           # int: 0 pawn, 1 knight, 2 bishop, 3 rook, 4 queen, 5 king
        self.color = 0          # int: 0 blanc, 1 noir
        self.coordinates = ()   # tupple[int,int] : [x,y]
        self.img = pygame.image.load("./assets/b_pawn.png")

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