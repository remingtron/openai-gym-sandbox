Execute tests by running `pytest` from command line

Next steps:
- Generate all non-terminal states and current turn
- For each state, calculate reward for potential move:
 - if move causes player to win, reward is +1
 - else, reward is 0
- Add this to negative Q value of next state to calculate target Q value, since it's then the opponent's turn.
- Backpropagate

Python notes:
- List comprehensions
