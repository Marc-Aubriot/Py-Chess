

class Piece:

    def __init__(self) -> None:
        self.id = "piece_num"   # str: uuid ?
        self.type = 0           # int: 0 pawn, 1 knight, 2 bishop, 3 rook, 4 queen, 5 king
        self.color = 0          # int: 0 blanc, 1 noir
        self.coordinates = []   # array[int,int] : [x,y]
        self.img = "str"

    # bouge la pièce à une destination
    def move(self):
        pass

    # vérifie les possibilités de mouvements de la pièce
    def check_move(self):
        pass

    # transforme un pion en une autre pièce
    def upgrade_pawn(self):
        pass