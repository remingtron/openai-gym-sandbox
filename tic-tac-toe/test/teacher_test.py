import unittest
import numpy
from tictactoe.teacher import Teacher


class TeacherTest(unittest.TestCase):

    def test_converts_empty_state_to_18_zeros(self):
        expected = numpy.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
        self.assert_converts_correctly(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1, expected)

    def test_converts_only_current_player_marks_correctly(self):
        expected = numpy.array([1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
        self.assert_converts_correctly(numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 1, expected)

    def test_converts_mixed_player_marks_correctly(self):
        expected = numpy.array([1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0., 1., 0., 0., 1., 0., 0.])
        self.assert_converts_correctly(numpy.array([[1, 2, 0], [2, 1, 0], [2, 0, 1]]), 1, expected)

    def assert_converts_correctly(self, state, player, expected):
        result = Teacher.convert_state_to_inputs(state, player)
        self.assertTrue(numpy.array_equal(result, expected), "expected: {}, got: {}".format(expected, result))
