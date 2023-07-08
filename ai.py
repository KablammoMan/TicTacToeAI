import tictactoe
import random
import json
import os

GAMES = 10**4

inputfile = open("poss.txt", "r")
input_line = inputfile.readline()
try:
    poss = json.loads(input_line)
except:
    poss = {}
inputfile.close()

for i in range(GAMES):
    thisgame = {"X": {}, "O": {}}
    game = tictactoe.new_game()
    player = "X"
    while tictactoe.check_game(game) == "CONTINUE":
        if not game in poss[player].keys():
            spaces = []
            for s_index, space in enumerate(game):
                if space == " ":
                    spaces.append(s_index)
            poss[player][game] = spaces
        thisgame[player][game] = poss[player][game][random.randint(0, len(poss[player][game])-1)]
        game = tictactoe.move(game, thisgame[player][game], player)
        if player == "X":
            player = "O"
        else:
            player = "X"
    os.system("cls")
    print(f"RUNNING {GAMES} TicTacToe Games")
    print(f"PROGRESS: {int((i+1)/GAMES*100*100)/100}%")

ouputfile = open("poss.txt", "w")
ouputfile.write(json.dumps(poss))
ouputfile.close()
