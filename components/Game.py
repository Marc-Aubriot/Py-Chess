import pygame 
from pygame import  *
from components.Board import Board
from components.HelperModule import HelperModule

class Game:

    def __init__(self, game_id) -> None:
        # app var
        self.id = game_id                                                                       # str: uuid?
        self.display_width = 1200                                                               # int: px
        self.display_height = 900                                                               # int: px
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
        self.active_piece = None                    # str: piece_id

        # starting game
        self.loop = self.main_loop()

    # la loop logique du jeu
    def main_loop(self):
        while True:
            # player inputs
            self.inputs()

            # do thing
            self.logic()

            # render
            self.render()

    # récupère les inputs du joueur avec pygame
    def inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            
            # click souris
            if event.type == pygame.MOUSEBUTTONDOWN:

                # left click
                if pygame.mouse.get_pressed()[0]:
                    x, y = event.pos

                    # si une piece est active vérifie que la case est un move possible
                    if self.active_piece != None:
                        temp_piece = self.get_piece_by_id(self.active_piece)
   
                        # check si le move est possible
                        if temp_piece.check_move(self.pieces, (x, y)) == True:
                            #chess_coordinates = self.get_chess_coordinates((x, y))

                            # update les coordonnées de la pièce et de la pièce dans la liste
                            coordinates = self.get_xy_coordinates((x, y))
                            temp_piece.move(coordinates)
                            self.pieces[temp_piece.piece_list_index].coordinates = (coordinates[0]*self.tile_size , coordinates[1]*self.tile_size)
                            print(coordinates)
                            print(self.pieces[temp_piece.piece_list_index].coordinates)

                    # vérifie si une pièce est sélectionnée en regardant les coordonnées des pièces et celles du click
                    for piece in self.pieces:
                        piece_body = piece.img.get_rect(topleft=(piece.coordinates[0], piece.coordinates[1]))

                        # collision affiche un curseur de sélection
                        if piece_body.collidepoint(x, y) and piece.selected == False and self.active_piece == None:

                            # si le joueur actif choisit une pièce adverse on ne fait rien
                            if self.active_player != piece.color:
                                return
                            piece.selected = True
                            self.active_piece = piece.id

                        # collision mais la pièce est déjà sélectionnée
                        elif piece_body.collidepoint(x, y) and piece.selected == True and self.active_piece != None:

                            # enlève le curseur de sélection
                            piece.selected = False
                            self.active_piece = None


                # right click
                elif pygame.mouse.get_pressed()[2]:
                    
                    # désélectionne la pièce actuellement sélectionnée
                    if self.active_piece != None:
                        temp_piece = self.get_piece_by_id(self.active_piece)
                        temp_piece.selected = False
                        self.active_piece = None

    # logic
    def logic(self):
        pass

    # dessine le jeu
    def render(self):
        pygame.display.flip()                                           # Refresh on-screen display
        self.display.fill(pygame.Color(255,255,255))                    # clear surface
        self.clock.tick(15)                                             # wait until next frame

        # dessine le plateau et les pièces
        self.board.draw(self.display)

        for piece in self.board.pieces_list:
            piece.draw(self.display)

            # si une pièce est selectionnée, place un curseur jaune sur la case
            if piece.selected == True:
                piece.draw_select_icon(self.display)
                piece.draw_moves(self.display, self.pieces)
            