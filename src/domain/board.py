import math

from src.exceptions.board_exceptions import Location_Not_Valid
import random
class Board:


    def __init__(self,rows,pieces_to_win, player_value):

        self.__row_count = rows
        self.__col_count = rows + 1
        self.__board = [[0 for _ in range (self.__col_count)] for _ in range (self.__row_count)]
        self.__pieces_to_win = pieces_to_win
        self.__player_value = player_value


    def get_board(self):
        """

        :return: the board
        """

        return self.__board

    def valid_location(self,col):
        """

        :param col: the column where we want to drop a piece
        :return: True if the column is not full yet, False otherwise
        """
        return self.__board[0][col] == 0

    def get_next_row(self,col):
        """

        :param col: the column where we want to drop a piece
        :return: the row where we can drop that piece
        """

        row = self.__row_count - 1
        while self.__board[row][col] != 0:
            row = row - 1
        return row

    def drop_piece(self,row,col, entity_value):
        """

        :param row: the row where we want to drop the piece
        :param col: the column where we want to drop the piece
        :param entity_value: the value we want to put at that place
        :return:
        """
        self.__board[row][col] = entity_value

    def remove_piece(self, row, col):
        """

        :param row: the row where we want to remove the piece
        :param col: the column where we want to remove the piece
        :return: -, empties the space at that place
        """
        self.__board[row][col] = 0



    def _search_horizontal(self,row,entity_value):
        """

        :param row: the row that is checked
        :param entity_value: the entity piece value it is checked for
        :return: all the points from that row
        """

        final_points = 0
        win = False
        start = 0
        end = self.__col_count - self.__pieces_to_win + 1

        for col in range (start, end):
            entity_pieces = 0
            enemy_pieces = 0
            check_col = col
            for _ in range (self.__pieces_to_win):
                if self.__board[row][check_col] == entity_value:
                    entity_pieces = entity_pieces + 1
                elif self.__board[row][check_col] != 0:
                    enemy_pieces = enemy_pieces + 1
                check_col = check_col + 1

            if entity_pieces == 4:
                win = True
            points = self.get_points (entity_pieces, enemy_pieces)
            final_points += points
        return final_points, win


    def _search_vertical(self,col,entity_value):
        """

        :param col: the column that is checked
        :param entity_value: the entity piece value it is checked for
        :return: all the points from that column
        """

        final_points = 0
        win = False
        start = 0
        end = self.__row_count - self.__pieces_to_win + 1

        for row in range (start, end):
            entity_pieces = 0
            enemy_pieces = 0
            check_row = row
            for _ in range (self.__pieces_to_win):
                if self.__board[check_row][col] == entity_value:
                    entity_pieces = entity_pieces + 1
                elif self.__board[check_row][col] != 0:
                    enemy_pieces = enemy_pieces + 1
                check_row = check_row + 1

            if entity_pieces == 4:
                win = True
            points = self.get_points (entity_pieces, enemy_pieces)
            final_points += points
        return final_points, win


    def _search_first_diagonal(self,row,col,entity_value):
        """

        :param row: the row we check
        :param col: the column we check
        :param entity_value: the entity piece value we look for
        :return: all the points obtained for that diagonal
        """

        start_row = 0
        end_row = self.__row_count - self.__pieces_to_win + 1
        start_col = 0
        end_col = self.__col_count - self.__pieces_to_win + 1

        while row > start_row and col > start_col:
            row = row - 1
            col = col - 1

        final_points = 0
        win = False

        while row < end_row and col < end_col:
            entity_pieces = 0
            enemy_pieces = 0
            check_row = row
            check_col = col
            for _ in range(self.__pieces_to_win):
                if self.__board[check_row][check_col] == entity_value:
                    entity_pieces = entity_pieces + 1
                elif self.__board[check_row][check_col] != 0:
                    enemy_pieces = enemy_pieces + 1
                check_row = check_row + 1
                check_col = check_col + 1

            if entity_pieces == 4:
                win = True
            points = self.get_points (entity_pieces, enemy_pieces)
            final_points += points



            row = row + 1
            col = col + 1
        return final_points, win


    def _search_second_diagonal(self, row, col, entity_value):
        """

        :param row: the row we check
        :param col: the column we check
        :param entity_value: the entity piece value we look for
        :return: all the points obtained for that diagonal
        """

        start_row = 0
        end_row = self.__row_count - self.__pieces_to_win + 1
        start_col = self.__col_count - 1
        end_col = self.__pieces_to_win - 1

        while row > start_row and col < start_col:
            row = row - 1
            col = col + 1

        final_points = 0
        win = False
        while row < end_row and col >= end_col:

            entity_pieces = 0
            enemy_pieces = 0
            check_row = row
            check_col = col


            for _ in range (self.__pieces_to_win):
                if self.__board[check_row][check_col] == entity_value:
                    entity_pieces = entity_pieces + 1
                elif self.__board[check_row][check_col] != 0:
                    enemy_pieces = enemy_pieces + 1
                check_row = check_row + 1
                check_col = check_col - 1

            if entity_pieces == 4:
                win = True
            points = self.get_points(entity_pieces, enemy_pieces)
            final_points += points

            row = row + 1
            col = col - 1
        return final_points, win


    def get_points(self, entity_pieces, enemy_pieces):
        """

        :param entity_pieces: the number of pieces of the entity we check
        :param enemy_pieces: the number of pieces of the enemy
        :return: the points for that 4 in a row
        """

        points = 0
        #check enemy
        if enemy_pieces == 2 and entity_pieces == 1:
            points = 10
        if enemy_pieces == 3 and entity_pieces == 1:
            points = 1000
        if enemy_pieces == 2 and entity_pieces == 0:
            points = -10
        if enemy_pieces == 3 and entity_pieces == 0:
            points = -1000

        if enemy_pieces == 0:
            if entity_pieces == 2:
                points = 8
            if entity_pieces == 3:
                points = 14
            if entity_pieces == 4:
                points = 1000000000
        return points



    def _get_move_points(self,col,entity_value):
        """

        :param col: the col where the piece was drop
        :param entity_value: the value of the entity that put a piece
        :return: all the points from the board after the last move
        """
        points = 0
        if col == self.__col_count // 2:
            points = 8

        for row in range(0, self.__row_count):

            points += self._search_horizontal (row, entity_value)[0]
            points += self._search_first_diagonal (row, 0, entity_value)[0]
            points += self._search_first_diagonal (0, row + 1, entity_value)[0]

        for col in range(0, self.__col_count):
            points += self._search_vertical (col, entity_value)[0]
            points += self._search_second_diagonal (0, col, entity_value)[0]

        for row in range(1, self.__row_count):
            points += self._search_second_diagonal(row, self.__col_count - 1, entity_value)[0]


        return points

    def get_winning_result(self, entity_value):
        """
        Checks the full board for winning
        :param entity_value: the value of the entity we check for winning
        :return: True if the entity won, False if not
        """

        winning = False

        for row in range(0, self.__row_count):

            if (self._search_horizontal (row, entity_value)[1] or
                self._search_first_diagonal (row, 0, entity_value)[1] or
                self._search_first_diagonal (0, row + 1, entity_value)[1]):

                winning = True

        for col in range(0, self.__col_count):
            if (self._search_vertical (col, entity_value)[1] or
                self._search_second_diagonal (0, col, entity_value)[1]):

                winning = True

        for row in range(1, self.__row_count):
            if self._search_second_diagonal(row, self.__col_count - 1, entity_value)[1]:
                winning = True

        return winning


    def make_move_player(self,col):
        """

        :param col: the col where to drop a piece
        :return: the state of winning and the winner after the move
        """
        if not self.valid_location(col):
            raise Location_Not_Valid()

        row = self.get_next_row (col)
        self.drop_piece(row,col, self.__player_value)

        win = self.get_winning_result(self.__player_value)

        ok_options = self.get_valid_locations ()
        if len (ok_options) == 0 and win == False:
            return True, "Draw"
        elif win == True:
            return True, "Player won"

        return False, None




    def get_valid_locations(self):
        """

        :return: list of columns where can be drop a piece
        """
        ok_options = []
        for col in range (self.__col_count):
            if self.valid_location (col):
                ok_options.append (col)

        return ok_options




class AI:

    def __init__(self, board:Board, player_value, AI_value, dificulty):
        self.__board = board
        self.__player_value = player_value
        self.__AI_value = AI_value
        self.__dificulty = dificulty




    def __make_normal_AI(self):
        """

        :return: the column where to drop a piece to get the best points for the AI
        """

        ok_options = self.__board.get_valid_locations()
        best_col = [ok_options[0]]
        max_points = 0
        for col in ok_options:
            row = self.__board.get_next_row (col)
            self.__board.drop_piece (row, col, self.__AI_value)
            points = self.__board._get_move_points (col, self.__AI_value)

            if points == max_points and col not in best_col:
                best_col.append (col)
            elif points > max_points:
                max_points = points
                best_col = [col]
            self.__board.remove_piece (row, col)
            print ()

        col = random.choice (best_col)
        return col

    def make_move_AI(self):
        """
        Makes the best move for the AI
        :return:the state of winning and the winner after the move
        """


        #col = self.__make_normal_AI()
        col, minmax_score = self.__minmax(self.__dificulty, True, 0)


        row = self.__board.get_next_row (col)
        self.__board.drop_piece (row, col, self.__AI_value)

        win = self.__board.get_winning_result (self.__AI_value)

        ok_options = self.__board.get_valid_locations ()
        if len (ok_options) == 0 and win == False:
            return True, "Draw"
        elif win == True:
            return True, "AI won"

        return False, None


    def is_terminal(self, ok_options):
        """

        :param ok_options: the places where there can be droped a piece
        :return: True if it is a terminal move, False if the game can go on
        """
        if self.__board.get_winning_result(self.__player_value):
            return True, "Player"
        if self.__board.get_winning_result(self.__AI_value):
            return True, "AI"
        if len(ok_options) == 0:
            return True, None
        return False, None

    def __minmax(self, depth, AI_turn, score):
        """

        :param depth: how far we look in the future
        :param AI_turn: bool, tells if it is the AI move or not
        :param score: the score obtained from the last move
        :return: the column where the AI should drop a piece
        """

        ok_options = self.__board.get_valid_locations ()
        terminal_move, winner = self.is_terminal(ok_options)

        if depth == 0 or terminal_move:

            if AI_turn and winner == 'Player':
                return (None, - 10000000)

            elif winner == "AI":
                return (None,  10000000)

            if terminal_move == True:
                return (None, 0)
            else:
                return (None, score)

        column = [ok_options[0]]


        if AI_turn:
            value = - math.inf

            for col in ok_options: #going through all the possibilities
                row = self.__board.get_next_row(col)
                self.__board.drop_piece(row,col, self.__AI_value)
                points = self.__board._get_move_points (col, self.__AI_value)

                new_score = self.__minmax(depth-1, False, points)[1] #searching in the future
                if new_score > value: # selecting the max solution
                    value = new_score
                    column = [col]
                elif new_score == value:
                    column.append (col)

                self.__board.remove_piece(row, col)


        else:


            value = math.inf
            for col in ok_options:
                row = self.__board.get_next_row (col)
                self.__board.drop_piece (row, col, self.__player_value)
                points = self.__board._get_move_points (col, self.__AI_value)
                new_score = self.__minmax (depth - 1, True, points)[1]

                if new_score < value:
                    value = new_score
                    column = [col]
                elif new_score == value:
                    column.append(col)

                self.__board.remove_piece (row, col)

        col = random.choice(column)
        return col, value




