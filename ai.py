import threading
import tictactoe
import random
import json
import os

def read_conf() -> dict:
    inputfile = open("aiconf.txt")
    input_line = inputfile.readline()
    if input_line != "":
        conf = json.loads(input_line)
    else:
        conf = {
            "amt_empty": 5,
            "train": 10000,
            "learn_player": 0
        }
        write_conf(conf)
    inputfile.close()
    return conf

def read_poss() -> dict:
    inputfile = open("poss.txt", "r")
    input_line = inputfile.read()
    if input_line != "":
        poss = json.loads(input_line)
    else:
        poss = {"X": {}, "O": {}}
        write_poss(poss)
    inputfile.close()
    return poss

def write_poss(poss: dict) -> None:
    ouputfile = open("poss.txt", "w")
    ouputfile.write(json.dumps(poss))
    ouputfile.close()

def write_conf(conf: dict) -> None:
    ouputfile = open("aiconf.txt", "w")
    ouputfile.write(json.dumps(conf))
    ouputfile.close()

def move(player: str, game: str) -> int:
    "Uses the knowledge it has to make a decision regarding what move to play in the scenario 'game' if its symbol is 'player'"
    poss = read_poss()

    if not game in poss[player].keys():
        p = []
        for i, s in enumerate(game):
            if s == " ":
                p.append(i)
        return p[random.randint(0, len(p)-1)]
    else:
        return poss[player][game][random.randint(0, len(poss[player][game])-1)]

def train(amt: int) -> None:
    """
    Trains the AI on 'amt' games. 'rand' is just cus threading was being annoying
    """
    GAMES = amt

    poss = read_poss()
    conf = read_conf()

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
                        for s in range(conf["amt_empty"]):
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

        # os.system("cls")
        print(f"RUNNING {GAMES} TicTacToe Games")
        print(f"PROGRESS: {int((i+1)/GAMES*100*100)/100}%")

    write_poss(poss)
    write_conf(conf)

def remove() -> None:
    f = open("poss.txt", "w")
    f.write("")
    f.close()

def game_result(moves: dict, player: str, result: str) -> None:
    poss = read_poss()
    conf = read_conf()
    if conf["learn_player"] != 0:
        if player == "X":
            ai = "O"
        else:
            ai = "X"
        if result != ai and result != "DRAW": # AI LOST
            for k,v in moves.items():
                if not k in poss[ai].keys():
                    sp = []
                    for si, i in enumerate(k):
                        if i == " ":
                            for s in range(conf["amt_empty"]):
                                sp.append(si)
                    sp.remove(v)
                    poss[ai][k] = sp
                else:
                    poss[ai][k].remove(v)
        elif result == "DRAW": # AI DREW
            for k,v in moves.items():
                if not k in poss[ai].keys():
                    sp = []
                    for si, i in enumerate(k):
                        if i == " ":
                            for s in range(conf["amt_empty"]):
                                sp.append(si)
                    sp.append(v)
                    poss[ai][k] = sp
                else:
                    poss[ai][k].append(v)
        else: # AI WON
            for k,v in moves.items():
                if not k in poss[ai].keys():
                    sp = []
                    for si, i in enumerate(k):
                        if i == " ":
                            for s in range(conf["amt_empty"]):
                                sp.append(si)
                    sp.append(v)
                    sp.append(v)
                    poss[ai][k] = sp
                else:
                    poss[ai][k].append(v)
                    poss[ai][k].append(v)
    write_poss(poss)
    write_conf(conf)

def train_thread(threads: int, amt: int):
    ts = []
    for i in range(threads):
        t = threading.Thread(target=train, args=[100], daemon=True)
        ts.append(t)
    for t in ts:
        t.start()
        t.join()
        print("Created New Thread")