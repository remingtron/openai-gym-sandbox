import numpy
import copy

from tictactoe.state import State


class StateGenerator:
    @staticmethod
    def generate(depth):
        initial_states = [State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1)]
        return StateGenerator.generate_from_states(initial_states, depth)

    @staticmethod
    def generate_from_states(states, depth):
        if depth == 0:
            return states
        new_states = {new_state for state in states if not state.winner() for new_state in StateGenerator.generate_next_states(state)}
        return states + StateGenerator.generate_from_states(list(new_states), depth - 1)

    @staticmethod
    def generate_next_states(state):
        return [StateGenerator.__add_move(row, column, state) for row in range(3) for column in range(3) if state.board[row, column] == 0]

    @staticmethod
    def __add_move(row, column, state):
        new_state = copy.copy(state)
        new_state.take_turn(row, column)
        return new_state
