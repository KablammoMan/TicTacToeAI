import tictactoe
import random
import time
import ai
import os

game = tictactoe.new_game()

print("Flipping a coin to see who goes first")
time.sleep(1)
os.system("cls")
if random.randint(0, 1) == 0: # Player goes first
    print("You are X (you go first)")
    clpl = "X"
else: # AI goes first
    print("You are O (you go second)")
    clpl = "O"

turn = "X"
aim = {}
while tictactoe.check_game(game) == "CONTINUE":
    if clpl == turn:
        pgam = tictactoe.print_game(game, True)
        inp = ""
        while not inp in pgam or len(inp) > 1 or not inp.isdigit():
            inp = input("Where do you want to move (must be a number shown): ")
        game = tictactoe.move(game, int(inp), turn)
    else:
        pgam = tictactoe.print_game(game, False)
        print("AI TURN")
        ait = ai.move(turn, game)
        aim[game] = ait
        game = tictactoe.move(game, ait, turn)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

winner = tictactoe.check_game(game)
ai.game_result(aim, clpl, winner)
if winner != "DRAW":
    print(f"{winner} WON!")
else:
    print("It was a tie...")