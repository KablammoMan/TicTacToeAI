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

def check_game(game: str) -> str:
    """
    Checks the specified game and returns either\n
    a) the symbol (X or O) of the winning player\n
    b) 'DRAW' if the game result is a draw\n
    c) 'CONTINUE' if the game should play on
    """
    for w in wins:
        if game[w[0]] == game[w[1]] == game[w[2]] and game[w[0]] != " ":
            return game[w[0]]
    if not " " in game:
        return "DRAW"
    return "CONTINUE"

def print_game(game: str, index: bool) -> None:
    """
    Prints out the specified game in a human readable format\n
    index (bool) - whether to print spaces as spaces, or the index of the game\n
    Returns the string that was printed
    """
    if not index:
        pgame = f"{game[0:3]}\n{game[3:6]}\n{game[6:9]}\n"
    else:
        pgame = ""
        for i, s in enumerate(game):
            if s == " ":
                pgame += i
            else:
                pgame += s
        pgame += "\n"
    print(pgame)
    return pgame

def move(game: str, move: int, turn: str) -> str:
    """
    Makes the specified move in the specified game and returns the new game array\n
    Returns False if the move is invalid\n
    game (str) - the string containing the current state of the game\n
    move (int) - the index of the position in 'game' string that is being requested to be changed\n
    turn (str) - the symbol of the player wanting to make that move ('X' or 'O')
    """
    if game[move] != " ":
        return False
    modgame = ""
    for i, s in enumerate(game):
        if i != move:
            modgame += s
        else:
            modgame += turn
    return modgame

def new_game() -> str:
    """Returns an empty sting with length of 9 to be used for a tic tac toe game"""
    return " " * 9