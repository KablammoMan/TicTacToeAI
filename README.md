# TicTacToeAI
My first attempt at making a simple neural networkless AI for a simple game

Based off that matchbox computer AI that had beads inside of matchboxes to represent moves in each scenario. Thank you to brilliant.org for teaching me how this old AI worked (not sponsored).

# aiconf.txt - The config file for the AI
- `amt_empty` (int, default=5) -- How many of each index should be inserted into list when a new scenario is discovered
- `learn_player` (int, default=0) -- If 0, AI does not learn when `game.py` is run. If any other value, will learn from player games.
