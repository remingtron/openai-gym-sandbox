from tictactoe.state import State


def print_state(state):
    print(state.board[0])
    print(state.board[1])
    print(state.board[2])

print('Welcome to tic-tac-toe!')

state = State()
print_state(state)
