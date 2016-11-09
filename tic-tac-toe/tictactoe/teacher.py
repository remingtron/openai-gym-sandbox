import numpy
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD


class Teacher:
    def calculate_q_values(self, state, player):
        print('a')

    @staticmethod
    def convert_state_to_inputs(state, player):
        current_player_state = (state.flatten() == player).astype(int)
        other_player_state = numpy.logical_and(state.flatten() > 0, state.flatten() != player).astype(int)
        return numpy.concatenate((current_player_state, other_player_state))

    @staticmethod
    def create_model():
        model = Sequential()
        model.add(Dense(12, input_dim=18, activation='relu', init='normal'))  # hidden layer, 18 inputs
        model.add(Dense(9, activation='sigmoid', init='normal'))  # output layer, one output for each space
        model.summary()

        optimizer = SGD(lr=0.1, momentum=0.9)
        model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['accuracy'])

