

class Player:

    def __init__(self, color, pieces) -> None:
        self.id = "player_id"   # str: uuid ?
        self.color = color      # int: 0 blanc, 1 noir
        self.pieces = pieces    # array[object*]: contenant les 16 pièces
        self.turn = None        # boolean

    # passe au tour suivant
    def turn_over(self):
        pass

    # prend une piece adverse
    def take_piece(self):
        pass

    # bouge une piece sur le plateau
    def move_piece(self):
        pass

    # met le roi adverse en échec
    def check(self):
        pass

    # met le roi adverse échec et mat 
    def check_mate(self):
        pass