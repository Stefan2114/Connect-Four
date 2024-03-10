from src.domain.board import Board, AI
from src.service.controller import Controller
from src.ui.console import Console
from src.ui.graphic_ui import Graphic_Console

if __name__ == '__main__':


    square_size = 100
    rows = 6
    pieces_to_win = 4
    player_value = 1
    AI_value = 2
    dificulty = 4
    player_starts_first = True
    board = Board(rows,pieces_to_win, player_value)
    ai = AI(board, player_value, AI_value, dificulty)
    controller = Controller(board, ai)
    #ui = Console(controller)
    ui = Graphic_Console(controller,square_size,rows)
    ui.start(player_starts_first)
