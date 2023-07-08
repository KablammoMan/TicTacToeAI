import tictactoe
import math
import random

inputfile = open("poss.txt", "r")
poss = dict(inputfile.readline())
inputfile.close()

for i in range(1000):
    thisgame = {}
    game = tictactoe.new_game()
    player = "X"
    while tictactoe.check_game(game) != "CONTINUE":
        if not game in poss.keys():
            poss[game] = [i for i in range(game.count(" "))]
        thisgame[game] = random.randint(0, poss[game][-1])
        game = tictactoe.move(game, thisgame[game], player)

ouputfile = open("poss.txt", "w")
ouputfile.write(poss)
ouputfile.close()
