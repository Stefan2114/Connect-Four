from src.domain.board import Board

class Controller:

    def __init__(self, board:Board, AI):
        self.__board = board
        self.__AI = AI


    def get_board(self):
        return self.__board.get_board()

    def make_move(self, col=None):
        if col == None:
            return self.__AI.make_move_AI()
        else:
            return self.__board.make_move_player(col-1)
