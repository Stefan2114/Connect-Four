import time
from colorama import Fore, Style


class Console:

    def __init__(self,serivce):
        self.__service = serivce


    def __print_board(self):
        board = self.__service.get_board()

        for row in board:
            for element in row:
                print(element, end=" ")
            print()



    def __player_move(self):

        col = input("The column you want to put a piece is >>>>")
        if col > '7' or col < '1':
            raise ValueError("The column must be between 1 and 7")
        game_over, end_state = self.__service.make_move (int(col))

        return game_over, end_state




    def __AI_move(self):
        game_over, end_state = self.__service.make_move ()
        return game_over, end_state

    def start(self, player_turn):

        game_over = False
        winner = None
        self.__print_board ()
        while not game_over:

            print()

            if player_turn:
                print("Player turn")
                try:
                    game_over, winner = self.__player_move()
                    player_turn = False
                except Exception as e:
                    print(Fore.RED + str(e) + Style.RESET_ALL)

            elif not game_over:
                print ("AI turn")
                time.sleep(1)
                game_over, winner = self.__AI_move()
                player_turn = True

            self.__print_board ()
            if game_over == True:
                print(winner + "!!!!")

            print()