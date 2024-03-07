import pygame 
from pygame import  *
from components.Board import Board
from components.HelperModule import HelperModule

class Game:

    def __init__(self, game_id) -> None:
        # app var
        self.id = game_id                                                                       # str: uuid?
        self.display_width = 800                                                               # int: px
        self.display_height = 800                                                               # int: px
        self.board_width = 800                                                                  # int: px
        self.board_height = 800                                                                 # int: px
        self.tile_size = self.board_width/8                                                     # int: px
        self.board = Board("board_one", self.board_width, self.board_height, self.tile_size)    # Surface   
        self.helper = HelperModule("helper")                                                    # Object: helper method

        # pygame var
        self.instance = pygame.init()
        self.title = pygame.display.set_caption("Py chess")
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.display_width,self.display_height))

        # game var
        self.turn_count = 0                         # int: le nombre de tour
        self.active_player = 0                      # int: player_id
        self.active_piece_id = None                 # str: piece_id
        self.a_king_is_checked = False              # bool: si un roi est échec
        self.turn_over = False

        # starting game
        self.loop = self.main_loop()

    # la loop logique du jeu
    def main_loop(self):
        while True:
            # player inputs
            self.inputs()

            if self.turn_over == True:
                self.turn_over = False
                self.next_turn()

            # render
            self.render()

    # récupère les inputs du joueur avec pygame
    def inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            
            # click souris
            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos

                # left click
                if pygame.mouse.get_pressed()[0]:
                    self.check_left_click((x, y))

                # right click
                elif pygame.mouse.get_pressed()[2]:
                    self.check_right_click((x, y))

    # dessine le jeu
    def render(self):
        pygame.display.flip()                                           # Refresh on-screen display
        self.display.fill(pygame.Color(255,255,255))                    # clear surface
        self.clock.tick(15)                                             # wait until next frame

        # dessine le plateau
        self.board.draw(self.display)

        # dessine les pièces
        for piece in self.board.pieces_list:
            piece.draw(self.display)

            # si une pièce est selectionnée
            if piece.id == self.active_piece_id:

                # place un curseur jaune sur la pièce
                self.board.draw_select_icon(self.display, piece)

                # montre les moves possibles en hightlightant les cases en vert
                self.board.draw_moves(self.display, piece, self.board.pieces_list)
            
            # si le roi est en échec
            if piece.is_checked == True:
                self.board.draw_king_is_checked(self.display, piece)
     
    # check input left click => sélectionne une pièce ou déplace une pièce active
    def check_left_click(self, event):
        x, y = event[0], event[1]
        piece = self.board.get_piece((x, y))

        # sélectionne la pièce
        if piece != None and self.active_piece_id == None and piece.color == self.active_player:
            self.active_piece_id = piece.id

            # si échec, regarde si les moves de la piece enlève l'échec
            if self.a_king_is_checked == True:
                if self.board.remove_checked_king(piece) == True :
                    print("cette piece peut interrompre l'échec")
                elif self.board.remove_checked_king(piece) == False :
                    self.active_piece_id = None
                    print("cette pièce ne peut pas interrompre l'échec")

        # déselectionne la pièce
        elif piece != None and self.active_piece_id == piece.id:
            self.active_piece_id = None

        # case vide sans sélection
        elif piece == None and self.active_piece_id == None:
            return
        
        # prise de pièce
        elif piece != None and self.active_piece_id != None:
            if piece.color != self.active_player:
                if self.board.take_piece(self.active_piece_id, (x, y)) == True:
                    self.turn_over = True
            elif piece.color == self.active_player:
                print("piece de la même couleur")

        # déplacement de pièce
        elif piece == None and self.active_piece_id != None:
            if self.board.move_piece(self.active_piece_id, (x, y)) == True:
                self.turn_over = True

    # check input right click => si une pièce est sélectionnée, l'enlève de la pièce active
    def check_right_click(self, event):
        if self.active_piece_id != None:
            self.active_piece_id = None

    # passe au tour suivant => switch le joueur et update les variables du jeu
    def next_turn(self):
        
        # switch le joueur
        if self.active_player == 0:
            self.active_player = 1
        else:
            self.active_player = 0
        
        # update les variables
        self.active_piece_id = None
        self.turn_count += 1

        # récupère les 2 rois
        white_king = self.helper.get_piece_by_id("white_king_1", self.board.pieces_list)
        black_king = self.helper.get_piece_by_id("black_king_1", self.board.pieces_list)

        # check si le roi blanc est échec
        if self.board.is_king_checked() == "white_king_check" and white_king.is_checked == False:
            white_king.is_checked = True
            self.a_king_is_checked = True
        elif white_king.is_checked == True and self.board.is_king_checked() == "no":
            white_king.is_checked = False
            self.a_king_is_checked = False

        # check si le roi noir est échec
        if self.board.is_king_checked() == "black_king_check" and black_king.is_checked == False:
            black_king.is_checked = True
            self.a_king_is_checked = True
        elif black_king.is_checked == True and self.board.is_king_checked() == "no":
            black_king.is_checked = False
            self.a_king_is_checked = False