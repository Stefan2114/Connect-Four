import unittest
from unittest import TestCase

from src.domain.board import Board, AI
from src.exceptions.board_exceptions import Location_Not_Valid


class FlightRepoTest (TestCase):
    def setUp(self):
        self._board = Board (6, 4, 1)
        self._AI = AI (self._board, 1, 2, 4)

    def test_drop_piece(self):
        self._board.drop_piece (5, 3, 1)
        self.assertEqual (self._board.get_board ()[5][3], 1)

        self._board.drop_piece (4, 6, 2)
        self.assertEqual (self._board.get_board ()[4][6], 2)

    def test_nex_row(self):
        self.assertEqual (self._board.get_next_row (2), 5)
        self._board.drop_piece (5, 3, 1)
        self.assertEqual (self._board.get_next_row (3), 4)

    def test_valid_location(self):
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 1)
        self.assertEqual (self._board.valid_location (3), True)

        row = self._board.get_next_row (5)
        self._board.drop_piece (row, 5, 1)
        self.assertEqual (self._board.valid_location (5), True)

        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 2)
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 2)
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 2)
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 1)
        self.assertEqual (self._board.valid_location (3), True)

        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 1)

        self.assertEqual (self._board.valid_location (3), False)

    def test_remove_piece(self):
        self._board.drop_piece (4, 6, 2)
        self._board.remove_piece (4, 6)
        self.assertEqual (self._board.get_board ()[4][6], 0)

        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 1)
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 2)
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 2)
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 2)
        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 1)

        row = self._board.get_next_row (3)
        self._board.drop_piece (row, 3, 1)
        self.assertEqual (self._board.valid_location (3), False)

        self._board.remove_piece (row, 3)
        self.assertEqual (self._board.valid_location (3), True)

    def test_get_points(self):
        self.assertEqual (self._board.get_points (0, 0), 0)
        self.assertEqual (self._board.get_points (1, 2), 10)
        self.assertEqual (self._board.get_points (1, 3), 1000)
        self.assertEqual (self._board.get_points (0, 2), -10)
        self.assertEqual (self._board.get_points (0, 3), -1000)
        self.assertEqual (self._board.get_points (2, 0), 8)
        self.assertEqual (self._board.get_points (3, 0), 14)
        self.assertEqual (self._board.get_points (4, 0), 1000000000)

    def test_get_winning_result(self):
        # check vertical
        self._board.drop_piece (5, 4, 1)
        self._board.drop_piece (4, 4, 1)
        self.assertEqual (self._board.get_winning_result (1), False)
        self._board.drop_piece (3, 4, 1)
        self._board.drop_piece (2, 4, 1)
        self.assertEqual (self._board.get_winning_result (1), True)

        self._board.remove_piece (5, 4)
        self._board.remove_piece (4, 4)
        self._board.remove_piece (3, 4)

        # check second diag
        self._board.drop_piece (3, 3, 1)
        self._board.drop_piece (0, 6, 1)
        self._board.drop_piece (1, 5, 1)
        self.assertEqual (self._board.get_winning_result (1), True)

        self._board.remove_piece (2, 4)
        self._board.remove_piece (3, 3)
        self._board.remove_piece (0, 6)
        self._board.remove_piece (1, 5)

        self._board.drop_piece (2, 1, 1)
        self._board.drop_piece (2, 2, 1)
        self._board.drop_piece (2, 3, 1)
        self._board.drop_piece (2, 4, 1)
        self.assertEqual (self._board.get_winning_result (1), True)

        self._board.remove_piece (2, 1)
        self._board.remove_piece (2, 2)
        self._board.remove_piece (2, 3)
        self._board.remove_piece (2, 4)

        self._board.drop_piece (0, 2, 1)
        self._board.drop_piece (1, 3, 1)
        self._board.drop_piece (2, 4, 1)
        self.assertEqual (self._board.get_winning_result (1), False)
        self._board.drop_piece (3, 5, 1)
        self.assertEqual (self._board.get_winning_result (1), True)

    def test_make_move_player(self):
        self.assertEqual (self._board.make_move_player (3), (False, None))
        self.assertEqual (self._board.make_move_player (2), (False, None))
        self.assertEqual (self._board.make_move_player (3), (False, None))
        self.assertEqual (self._board.make_move_player (3), (False, None))
        self.assertEqual (self._board.make_move_player (3), (True, "Player won"))
        self._board.remove_piece (3, 2)
        self._board.drop_piece (3, 2, 2)
        self._board.make_move_player (3)
        self._board.make_move_player (3)
        self.assertRaises(Location_Not_Valid, self._board.make_move_player, 3)


    def test_get_valid_locations(self):
        self._board.drop_piece (3, 3, 2)
        self._board.drop_piece (2, 3, 2)
        self._board.drop_piece (2, 6, 2)
        self._board.drop_piece (1, 3, 2)
        self.assertEqual (self._board.get_valid_locations (), [0, 1, 2, 3, 4, 5, 6])
        self._board.drop_piece (0, 3, 2)
        self.assertEqual (self._board.get_valid_locations (), [0, 1, 2, 4, 5, 6])

        self._board.drop_piece (0, 2, 1)
        self._board.drop_piece (0, 1, 1)
        self.assertEqual (self._board.get_valid_locations (), [0, 4, 5, 6])

        self._board.drop_piece (0, 0, 2)
        self.assertEqual (self._board.get_valid_locations (), [4, 5, 6])

    def test_is_terminal(self):
        self._board.drop_piece (0, 0, 2)
        self._board.drop_piece (0, 1, 1)
        self._board.drop_piece (0, 2, 1)
        self._board.drop_piece (0, 3, 2)
        self._board.drop_piece (0, 4, 1)
        self._board.drop_piece (0, 5, 2)
        ok_options = self._board.get_valid_locations ()
        self.assertEqual (self._AI.is_terminal (ok_options), (False, None))
        self._board.drop_piece (0, 6, 2)
        ok_options = self._board.get_valid_locations ()
        self.assertEqual (self._AI.is_terminal (ok_options), (True, None))

        self._board.remove_piece (0, 6)
        self._board.remove_piece (0, 5)
        self._board.remove_piece (0, 4)
        self._board.remove_piece (0, 3)
        self._board.remove_piece (0, 2)

        self._board.drop_piece (1, 1, 2)
        self._board.drop_piece (2, 2, 2)
        self._board.drop_piece (3, 3, 2)

        ok_options = self._board.get_valid_locations ()
        self.assertEqual (self._AI.is_terminal (ok_options), (True, "AI"))

        self._board.remove_piece (1, 1)
        self._board.remove_piece (2, 2)
        self._board.remove_piece (3, 3)

        self._board.drop_piece (1, 1, 1)
        self._board.drop_piece (2, 1, 1)
        self._board.drop_piece (3, 1, 2)

        ok_options = self._board.get_valid_locations ()
        self.assertEqual (self._AI.is_terminal (ok_options), (False, None))

        self._board.drop_piece (3, 1, 1)

        ok_options = self._board.get_valid_locations ()
        self.assertEqual (self._AI.is_terminal (ok_options), (True, "Player"))


if __name__ == '__main__':
    unittest.main ()
