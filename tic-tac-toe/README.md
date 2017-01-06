Execute tests by running `pytest` from command line

Next steps:
- Done - Generate all non-terminal states and current turn
- For each state, calculate reward for potential move:
 - if space is already occupied, treat as loss (reward is -1)
 - if move causes player to win, reward is +1
 - else, reward is -Q value of next state (calculated for other player)
 - if no move can be made, Q value is 0
- Backpropagate

Python notes:
- List comprehensions
