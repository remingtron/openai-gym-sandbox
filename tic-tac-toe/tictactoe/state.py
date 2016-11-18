import numpy

class State:
    def __init__(self, board, current_player):
        self.board = board
        self.current_player = current_player

    def __eq__(self, other):
        return numpy.array_equal(self.board, other.board) and self.current_player == other.current_player

    def __str__(self):
        return "<State board: >"
