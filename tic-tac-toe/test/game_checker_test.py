from tictactoe.game_checker import GameChecker
import numpy
import unittest


class GameCheckerTest(unittest.TestCase):
    def test_returns_false_for_empty_game(self):
        self.assertFalse(GameChecker.won_game(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1))

    def test_returns_true_if_first_row_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]), 1))

    def test_returns_false_if_only_first_position_belongs_to_player(self):
        self.assertFalse(GameChecker.won_game(numpy.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), 1))

    def test_returns_true_if_second_row_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]), 1))

    def test_returns_true_if_third_row_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]]), 1))

    def test_returns_true_if_first_column_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]]), 1))

    def test_returns_true_if_second_column_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 1))

    def test_returns_true_if_third_column_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]]), 1))

    def test_returns_true_if_first_diagonal_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 1))

    def test_returns_true_if_second_diagonal_all_belong_to_player(self):
        self.assertTrue(GameChecker.won_game(numpy.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 1))
