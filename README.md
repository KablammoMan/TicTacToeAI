# TicTacToeAI
My first attempt at making a simple neural networkless AI for a simple game

Based off that matchbox computer AI that had beads inside of matchboxes to represent moves in each scenario. Thank you to brilliant.org for teaching me how this old AI worked (not sponsored).

# aiconf.txt - The config file for the AI
- `amt_empty` (int, default=3) -- How many of each index should be inserted into list when a new scenario is discovered
- `learn_player` (int, default=1) -- If 0, AI does not learn when `game.py` is run. If any other value, will learn from player games.

# AUTHOR"S NOTE
The only *'effective'* way for the AI to learn is by playing games against a human player with `learn_player` set to 1 in `aiconf.txt`. This is due to the `train.py` script only training the AI against itself, which means it can reward a move that was actually bad, but only worked because it was playing another copy of itself, which chose randomly and had no strategy behind its moves. I may implement a win checker script in `ai.py` that sees whether either player can win in one move, and thus, change limit the possible spaces to ones that will make it win or stop the opponent from winning.