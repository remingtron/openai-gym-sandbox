import unittest
import numpy

from tictactoe.state import State
from tictactoe.state_generator import StateGenerator


class GameCheckerTest(unittest.TestCase):
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
