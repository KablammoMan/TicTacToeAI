wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def check_game(game):
    for w in wins:
        if game[w[0]] == game[w[1]] == game[w[2]]:
            return game[w[0]]
    if not " " in game:
        return "DRAW"
    return False

def print_game(game):
    print(f"{game[0:3]}\n{game[3:6]}\n{game[6:9]}\n")