import unittest
import numpy

from tictactoe.state import State
from tictactoe.state_generator import StateGenerator


class StateGeneratorTest(unittest.TestCase):
    def test_returns_single_state_when_zero_turns_have_been_taken(self):
        states = StateGenerator.generate(0)
        self.assertCountEqual([State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1)], states)

    def test_returns_ten_states_when_depth_is_one(self):
        states = StateGenerator.generate(1)
        expected_states = [
            State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1),
            State(numpy.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), 2),
            State(numpy.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]]), 2),
            State(numpy.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]]), 2),
            State(numpy.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]]), 2),
            State(numpy.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2),
            State(numpy.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]]), 2),
            State(numpy.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]]), 2),
            State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 1, 0]]), 2),
            State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]]), 2)
        ]
        self.assertCountEqual(expected_states, states)

    def test_generate_from_states_filters_out_terminal_states_from_generating_more_states(self):
        input_states = [
            State(numpy.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]), 2),
            State(numpy.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), 2)
        ]
        output_states = StateGenerator.generate_from_states(input_states, 1)
        expected_states = [
            State(numpy.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]), 2),
            State(numpy.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), 2),
            State(numpy.array([[1, 2, 0], [0, 0, 0], [0, 0, 0]]), 1),
            State(numpy.array([[1, 0, 2], [0, 0, 0], [0, 0, 0]]), 1),
            State(numpy.array([[1, 0, 0], [2, 0, 0], [0, 0, 0]]), 1),
            State(numpy.array([[1, 0, 0], [0, 2, 0], [0, 0, 0]]), 1),
            State(numpy.array([[1, 0, 0], [0, 0, 2], [0, 0, 0]]), 1),
            State(numpy.array([[1, 0, 0], [0, 0, 0], [2, 0, 0]]), 1),
            State(numpy.array([[1, 0, 0], [0, 0, 0], [0, 2, 0]]), 1),
            State(numpy.array([[1, 0, 0], [0, 0, 0], [0, 0, 2]]), 1),
        ]
        self.assertCountEqual(output_states, expected_states)

    def test_generate_next_states_adds_current_player_to_each_open_spot(self):
        states = StateGenerator.generate_next_states(State(numpy.array([[0, 1, 0], [1, 2, 0], [2, 0, 1]]), 2))
        self.assertCountEqual(states, [
            State(numpy.array([[2, 1, 0], [1, 2, 0], [2, 0, 1]]), 1),
            State(numpy.array([[0, 1, 2], [1, 2, 0], [2, 0, 1]]), 1),
            State(numpy.array([[0, 1, 0], [1, 2, 2], [2, 0, 1]]), 1),
            State(numpy.array([[0, 1, 0], [1, 2, 0], [2, 2, 1]]), 1)
        ])
