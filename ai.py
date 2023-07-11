import tictactoe
import random
import json
import os

def move(player: str, game: str) -> None:
    inputfile = open("poss.txt", "r")
    input_line = inputfile.read()
    if input_line != "":
        poss = json.loads(input_line)
    else:
        poss = False
    inputfile.close()

    if not poss:
        p = []
        for i, s in enumerate(game):
            if s == " ":
                p.append(i)
        return p[random.randint(0, len(p)-1)]
    elif not poss[player][game] in poss[player].keys():
        p = []
        for i, s in enumerate(game):
            if s == " ":
                p.append(i)
        return p[random.randint(0, len(p)-1)]
    else:
        return poss[player][game][random.randint(0, len(poss[player][game])-1)]

def train(amt: int) -> None:
    GAMES = amt

    inputfile = open("poss.txt", "r")
    input_line = inputfile.readline()
    if input_line != "":
        poss = json.loads(input_line)
    else:
        poss = {"X": {}, "O": {}}
    inputfile.close()

    for i in range(GAMES):
        thisgame = {"X": {}, "O": {}}
        game = tictactoe.new_game()
        if i % 2 == 0:
            player = "X"
        else:
            player = "O"
        while tictactoe.check_game(game) == "CONTINUE":
            if not game in poss[player].keys():
                spaces = []
                for s_index, space in enumerate(game):
                    if space == " ":
                        for s in range(5):
                            spaces.append(s_index)
                poss[player][game] = spaces
            thisgame[player][game] = poss[player][game][random.randint(0, len(poss[player][game])-1)]
            game = tictactoe.move(game, thisgame[player][game], player)
            if player == "X":
                player = "O"
            else:
                player = "X"
        winner = tictactoe.check_game(game)
        if winner != "DRAW":
            for k,v in thisgame[winner].items():
                poss[winner][k].append(v)
                poss[winner][k].append(v)
            if winner == "X":
                loser = "O"
            else:
                loser = "X"
            for k,v in thisgame[loser].items():
                if len(poss[loser][k]) > 1:
                    poss[loser][k].remove(v)
        else:
            for k,v in thisgame["X"].items():
                poss["X"][k].append(v)
            for k,v in thisgame["O"].items():
                poss["O"][k].append(v)

        os.system("cls")
        print(f"RUNNING {GAMES} TicTacToe Games")
        print(f"PROGRESS: {int((i+1)/GAMES*100*100)/100}%")

    ouputfile = open("poss.txt", "w")
    ouputfile.write(json.dumps(poss))
    ouputfile.close()
