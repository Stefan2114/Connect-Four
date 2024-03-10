import sys
import time
import pygame

class Graphic_Console:


    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    WHITE = (255, 255, 255)

    def __init__(self,serivce,square_size,rows):
        self.__service = serivce
        self.__square_size = square_size
        self.__row_count = rows
        self.__col_count = rows + 1
        self.__width = square_size * (rows + 1)
        self.__height = square_size * (rows + 1)
        self.__size = (self.__width, self.__height)
        self.__radius = self.__square_size//2.2




    def __draw_board(self,screen):

        square_size = self.__square_size
        board = self.__service.get_board()

        for col in range (self.__col_count):
            for row in range (self.__row_count):
                pygame.draw.rect(screen, Graphic_Console.BLUE,
                                 (col* square_size, row * square_size + square_size, square_size, square_size))
                COLOR = Graphic_Console.BLACK
                if board[row][col] == 1:
                    COLOR = Graphic_Console.RED
                elif board[row][col] == 2:
                    COLOR = Graphic_Console.YELLOW

                pygame.draw.circle (screen, COLOR,(col * square_size + square_size//2, row * square_size + square_size + square_size//2),self.__radius)


    def __draw_game_over(self, screen, winner):

        pygame.draw.rect (screen, Graphic_Console.BLACK, (0, 0, self.__width, self.__square_size))

        font = pygame.font.Font (None, int(self.__square_size / 1.5))
        text = font.render (winner, True, Graphic_Console.WHITE)

        # Calculate position to center text on the top
        text_rect = text.get_rect (center=(self.__width // 2 - len(winner)//2, self.__square_size // 2))
        screen.blit (text, text_rect)


    def __draw_screen(self, screen, game_over, winner):

        self.__draw_board (screen)
        if game_over:
            self.__draw_game_over (screen, winner)
        pygame.display.update ()


    def __draw_ball_option(self, screen, posX):

        pygame.draw.rect(screen, Graphic_Console.BLACK, (0,0, self.__width, self.__square_size))
        COLOR = Graphic_Console.RED
        col = posX // self.__square_size
        pygame.draw.circle(screen, COLOR, (col * self.__square_size + self.__square_size // 2, self.__square_size // 2), self.__radius)




    def __player_move(self, posX):
        col = posX//self.__square_size
        game_over, end_state = self.__service.make_move(col + 1)
        return game_over, end_state





    def __AI_move(self):
        game_over, end_state = self.__service.make_move ()
        return game_over, end_state


    def start(self, player_turn):

        pygame.init()
        screen = pygame.display.set_mode(self.__size)
        screen.fill (Graphic_Console.BLACK)
        game_over = False
        self.__draw_screen (screen, game_over, None)
        winner = None
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if not game_over:

                    if player_turn:

                        if event.type == pygame.MOUSEMOTION:

                            posX = event.pos[0]
                            self.__draw_ball_option(screen, posX,)

                        if event.type == pygame.MOUSEBUTTONDOWN:

                            posX = event.pos[0]
                            try:
                                game_over, winner = self.__player_move(posX)
                                player_turn = False

                            except:
                                pass

                    else:

                        time.sleep(1)
                        game_over, winner = self.__AI_move()
                        player_turn = True


                    self.__draw_screen(screen, game_over, winner)


