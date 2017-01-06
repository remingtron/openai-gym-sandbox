import unittest
import numpy

from tictactoe.state import State


class StateTest(unittest.TestCase):

    def test_defaults_state_and_turn(self):
        self.assertTrue(numpy.array_equal(State().board, numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])))
        self.assertEqual(State().current_player, 1)

    def test_take_turn_adds_current_player_to_specified_position(self):
        state = State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1)
        state.take_turn(1, 2)
        self.assertTrue(numpy.array_equal(state.board, numpy.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])))

    def test_take_turn_switches_from_player_one_to_player_two(self):
        state = State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1)
        state.take_turn(1, 2)
        self.assertEqual(state.current_player, 2)

    def test_take_turn_switches_from_player_two_to_player_one(self):
        state = State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 2)
        state.take_turn(1, 2)
        self.assertEqual(state.current_player, 1)

    def test_two_states_are_equal_if_they_have_the_same_board_and_current_player(self):
        first_state = State(numpy.array([[2, 0, 1], [0, 1, 0], [0, 0, 0]]), 2)
        second_state = State(numpy.array([[2, 0, 1], [0, 1, 0], [0, 0, 0]]), 2)
        self.assertEqual(first_state, second_state)

    def test_equals_returns_false_if_non_state_is_passed(self):
        state = State(numpy.array([0, 0, 0]), 1)
        self.assertFalse(state == 3)

    def test_winner_returns_zero_for_empty_game(self):
        self.assertEqual(0, State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1).winner())

    def test_winner_returns_one_if_first_row_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]), 1).winner())

    def test_returns_zero_if_only_first_position_belongs_to_player(self):
        self.assertEqual(0, State(numpy.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), 1).winner())

    def test_returns_one_if_second_row_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]), 1).winner())

    def test_returns_one_if_third_row_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]]), 1).winner())

    def test_returns_one_if_first_column_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]]), 1).winner())

    def test_returns_one_if_second_column_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 1).winner())

    def test_returns_one_if_third_column_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]]), 1).winner())

    def test_returns_one_if_first_diagonal_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 1).winner())

    def test_returns_one_if_second_diagonal_all_belong_to_player_one(self):
        self.assertEqual(1, State(numpy.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 1).winner())

    def test_returns_two_if_second_diagonal_all_belong_to_player_two(self):
        self.assertEqual(2, State(numpy.array([[0, 0, 2], [0, 2, 0], [2, 0, 0]]), 1).winner())

    def test_returns_zero_if_no_winner(self):
        self.assertEqual(0, State(numpy.array([[1, 1, 2], [2, 2, 1], [1, 1, 2]]), 1).winner())
