import numpy


class Teacher:
    def calculate_q_values(self, state, player):
        print('a')

    @staticmethod
    def convert_state_to_inputs(state, player):
        current_player_state = (state.flatten() == player).astype(int)
        other_player_state = numpy.logical_and(state.flatten() > 0, state.flatten() != player).astype(int)
        return numpy.concatenate((current_player_state, other_player_state))

