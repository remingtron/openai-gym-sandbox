import numpy
import copy


class State:
    def __init__(self, board, current_player):
        self.board = board
        self.current_player = current_player

    def take_turn(self, row, column):
        self.board[row, column] = self.current_player
        self.current_player = 1 if self.current_player == 2 else 2

    def winner(self):
        return self.__winner_in_row(0) or \
               self.__winner_in_row(1) or \
               self.__winner_in_row(2) or \
               self.__winner_in_column(0) or \
               self.__winner_in_column(1) or \
               self.__winner_in_column(2) or \
               self.__winner_on_first_diagonal() or \
               self.__winner_on_second_diagonal()

    def __eq__(self, other):
        return isinstance(other, State) and numpy.array_equal(self.board, other.board) and self.current_player == other.current_player

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return "<State board: {}, current player: {}>".format(self.board, self.current_player).replace("\n", "")

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        return State(copy.copy(self.board), copy.copy(self.current_player))

    def __winner_in_row(self, row):
        return self.board[row, 0] if self.board[row, 0] != 0 and self.board[row, 0] == self.board[row, 1] and self.board[row, 0] == self.board[row, 2] else 0

    def __winner_in_column(self, column):
        return self.board[0, column] if self.board[0, column] != 0 and self.board[0, column] == self.board[1, column] and self.board[0, column] == self.board[2, column] else 0

    def __winner_on_first_diagonal(self):
        return self.board[0, 0] if self.board[0, 0] != 0 and self.board[0, 0] == self.board[1, 1] and self.board[0, 0] == self.board[2, 2] else 0

    def __winner_on_second_diagonal(self):
        return self.board[0, 2] if self.board[0, 2] != 0 and self.board[0, 2] == self.board[1, 1] and self.board[0, 2] == self.board[2, 0] else 0
