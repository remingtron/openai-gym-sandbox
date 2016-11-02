class GameChecker:
    @staticmethod
    def won_game(state, player):
        return GameChecker.won_in_row(player, state, 0) or \
               GameChecker.won_in_row(player, state, 1) or \
               GameChecker.won_in_row(player, state, 2) or \
               GameChecker.won_in_column(player, state, 0) or \
               GameChecker.won_in_column(player, state, 1) or \
               GameChecker.won_in_column(player, state, 2) or \
               GameChecker.won_on_first_diagonal(player, state) or \
               GameChecker.won_on_second_diagonal(player, state)

    @staticmethod
    def won_in_row(player, state, row):
        return state[row, 0] == player and state[row, 1] == player and state[row, 2] == player

    @staticmethod
    def won_in_column(player, state, column):
        return state[0, column] == player and state[1, column] == player and state[2, column] == player

    @staticmethod
    def won_on_first_diagonal(player, state):
        return state[0, 0] == player and state[1, 1] == player and state[2, 2] == player

    @staticmethod
    def won_on_second_diagonal(player, state):
        return state[0, 2] == player and state[1, 1] == player and state[2, 0] == player
