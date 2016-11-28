Execute tests by running `pytest` from command line

Next steps:
- Generate all non-terminal states and current turn
- For each state, calculate reward for potential move:
 - if move causes player to win, reward is +1
 - else, reward is 1 minus Q value of next state (calculated for other player)
 - if no move can be made, Q value is 0.5
- Backpropagate

Python notes:
- List comprehensions
