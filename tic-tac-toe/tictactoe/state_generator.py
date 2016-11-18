import numpy

from tictactoe.state import State


class StateGenerator:
    @staticmethod
    def generate(depth):
        initial_states = [State(numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1)]
        return StateGenerator.__generate(initial_states, depth)

    @staticmethod
    def __generate(states, depth):
        if depth == 0:
            return states
        return [new_state for state in states for new_state in StateGenerator.generate_next_states(state)]

    @staticmethod
    def generate_next_states(state):
        next_player = 2 if state.current_player == 1 else 1
        return []

